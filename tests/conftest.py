import os
import socket
import time

import etcd3
import pymemcache
import pymemcache.client
import pymongo
import pytest
import redis as r

import kv_benchmark


def check_redis_cluster_ready(host, port):
    try:
        return r.Redis(host, port).cluster("info")["cluster_state"] == "ok"
    except Exception:
        return False


def check_mongo_ready(host, port):
    try:
        pymongo.MongoClient("mongodb://localhost:37017").server_info()

        return True
    except:  # noqa
        return False


def check_etcd_ready(host, port):
    try:
        etcd3.client(host, port).status()

        return True
    except:  # noqa
        return False


@pytest.fixture(scope="session")
def host_ip_env():
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    try:
        s.connect(("10.255.255.255", 1))
        ip = s.getsockname()[0]
    except Exception:
        ip = "127.0.0.1"
    finally:
        s.close()
    os.environ["HOST_IP"] = str(ip)


@pytest.fixture(scope="session")
def docker_services(host_ip_env, docker_services):
    return docker_services


@pytest.fixture(scope="session")
def etcd_client(docker_services):
    docker_services.start("etcd")
    docker_services.wait_for_service("etcd", 2379, check_etcd_ready)

    if os.environ.get("CI") == "True":
        time.sleep(5)

    return etcd3.client()


@pytest.fixture(scope="session")
def redis_client(docker_services):
    docker_services.start("redis")

    return r.StrictRedis("localhost", 7379)


@pytest.fixture(scope="session")
def dragonfly_client(docker_services):
    docker_services.start("dragonfly")
    time.sleep(5)
    return r.StrictRedis("localhost", 10379)

@pytest.fixture(scope="session")
def keydb_client(docker_services):
    docker_services.start("keydb")
    time.sleep(5)
    return r.StrictRedis("localhost", 11379)


@pytest.fixture(scope="session")
def redis_cluster_client(docker_services):
    docker_services.start("redis-cluster-init")
    docker_services.wait_for_service("redis-cluster-6", 7006, check_redis_cluster_ready)

    return r.cluster.RedisCluster("localhost", 7001)


@pytest.fixture(scope="session")
def memcached_client(docker_services):
    docker_services.start("memcached-1")

    return pymemcache.Client(("localhost", 22122))


@pytest.fixture(scope="session")
def mongodb_client(docker_services):
    docker_services.start("mongodb")
    docker_services.wait_for_service("mongodb", 27017, check_mongo_ready)

    return pymongo.MongoClient("mongodb://localhost:37017")


@pytest.fixture
def memcached(memcached_client):
    memcached_client.flush_all()
    memcached_client.set("fubar", 1)
    return kv_benchmark.Memcached(memcached_client)


@pytest.fixture
def redis(redis_client):
    redis_client.flushall()
    redis_client.set("fubar", 1)

    return kv_benchmark.Redis(redis_client)


@pytest.fixture
def dragonfly(dragonfly_client):
    dragonfly_client.flushall()
    dragonfly_client.set("fubar", 1)

    return kv_benchmark.Redis(dragonfly_client)

@pytest.fixture
def keydb(keydb_client):
    keydb_client.flushall()
    keydb_client.set("fubar", 1)

    return kv_benchmark.Redis(keydb_client)


@pytest.fixture
def redis_cluster(redis_cluster_client):
    redis_cluster_client.flushall()
    redis_cluster_client.set("fubar", 1)

    return kv_benchmark.Redis(redis_cluster_client)


@pytest.fixture
def mongodb(mongodb_client):
    mongodb_client.bm.space.drop()
    mongodb_client.bm.space.insert_one({"_id": "fubar", "value": 1})
    return kv_benchmark.Mongo(mongodb_client, "bm")


@pytest.fixture
def etcd(etcd_client):
    etcd_client.put(b"fubar", b"1")
    return kv_benchmark.Etcd(etcd_client)


@pytest.fixture(scope="session")
def docker_services_project_name():
    return "python-kv-benchmark"


@pytest.fixture(scope="session")
def docker_compose_files(pytestconfig):
    """Get the docker-compose.yml absolute path.
    Override this fixture in your tests if you need a custom location.
    """

    return ["docker-compose.yml"]
