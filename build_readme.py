import etcd3
import pymemcache
import pymemcache.client
import pymongo
import redis

import kv_benchmark


def versions_string():
    servers = {
        "Redis": kv_benchmark.Redis(redis.Redis(port=7379)),
        "Dragonfly": kv_benchmark.Redis(redis.Redis(port=10379)),
        "Memcached": kv_benchmark.Memcached(pymemcache.Client(("localhost", 22122))),
        "Redis Cluster": kv_benchmark.Redis(
            redis.cluster.RedisCluster("localhost", 7001)
        ),
        "MongoDB": kv_benchmark.Mongo(
            pymongo.MongoClient("mongodb://localhost:37017"), "bm"
        ),
        "Etcd": kv_benchmark.Etcd(etcd3.client()),
    }
    versions_str = ""
    for name, store in servers.items():
        versions_str += f"- {name}: {store.version()}\n"
    return versions_str


tmpl = open("README.tmpl").read()
tmpl = tmpl.replace("{TABLE}", open("results/table.txt").read())
tmpl = tmpl.replace("{VERSIONS}", versions_string())
open("README.md", "w").write(tmpl)
