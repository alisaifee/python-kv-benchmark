import abc
from typing import Any, cast

import etcd3
import pymemcache
import pymemcache.client
import pymongo
import redis


class Store(metaclass=abc.ABCMeta):
    @abc.abstractmethod
    def get(self, key: str) -> Any:
        ...

    @abc.abstractmethod
    def set(self, key: str, value: str) -> None:
        ...

    @abc.abstractmethod
    def incr(self, key: str) -> int:
        ...

    @abc.abstractmethod
    def version(self) -> str:
        ...


class Redis(Store):
    def __init__(self, client: redis.Redis) -> None:
        self.client = client

    def get(self, key: str) -> Any:
        return cast(str, self.client.get(key))

    def set(self, key: str, value: str) -> None:
        self.client.set(key, value)

    def incr(self, key: str) -> int:
        return self.client.incrby(key, 1)

    def version(self) -> str:
        return self.client.info()["redis_version"]


class Memcached(Store):
    def __init__(self, client: pymemcache.client.Client) -> None:
        self.client = client

    def get(self, key: str) -> Any:
        return cast(str, self.client.get(key))

    def set(self, key: str, value: str) -> None:
        self.client.set(key, value)

    def incr(self, key: str) -> int:
        return self.client.incr(key, 1)

    def version(self) -> str:
        return self.client.stats()[b"version"].decode("utf-8")


class Etcd(Store):
    def __init__(self, client: etcd3.Etcd3Client) -> None:
        self.client = client

    def get(self, key: str) -> Any:
        return cast(str, self.client.get(key.encode())[0])

    def set(self, key: str, value: str) -> None:
        self.client.put(key.encode(), value.encode())

    def incr(self, key: str) -> int:
        create_result = self.client.transaction(
            [self.client.transactions.create(key.encode()) == b"0"],
            [self.client.transactions.put(key.encode(), b"1")],
            [self.client.transactions.get(key.encode())],
        )

        if create_result[0]:
            return 1
        else:
            cur_value = create_result[1][0][0][0]
            while not (
                update_result := self.client.transaction(
                    [self.client.transactions.value(key.encode()) == cur_value],
                    [
                        self.client.transactions.put(
                            key.encode(), str(int(cur_value) + 1).encode()
                        )
                    ],
                    [self.client.transactions.get(key.encode())],
                )
            )[0]:
                cur_value = update_result[1][0][0][0]

            return int(cur_value) + 1

    def version(self) -> str:
        return self.client.status().version


class Mongo(Store):
    def __init__(self, client: pymongo.MongoClient, db: str) -> None:
        self.client = client
        self.collection = self.client.get_database(db).space

    def get(self, key: str) -> Any:
        obj = self.collection.find_one(
            {"_id": key},
            projection=["value"],
        )

        if obj:
            return cast(str, obj["value"])

    def set(self, key: str, value: str) -> None:
        self.collection.replace_one({"_key": key}, {"value": value}, upsert=True)

    def incr(self, key: str) -> int:
        return self.collection.find_one_and_update(
            {"_key": key},
            [
                {
                    "$set": {
                        "value": {
                            "$cond": {
                                "if": {"$lt": ["$value", 0]},
                                "then": 1,
                                "else": {"$add": ["$value", 1]},
                            }
                        }
                    }
                }
            ],
            upsert=True,
            projection=["value"],
            return_document=pymongo.ReturnDocument.AFTER,
        )["value"]

    def version(self) -> str:
        return self.client.server_info()["version"]
