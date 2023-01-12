import platform

import etcd3
import psutil
import pymemcache
import pymemcache.client
import pymongo
import redis

import kv_benchmark


def get_size(bytes, suffix="B"):
    """
    Scale bytes to its proper format
    e.g:
        1253656 => '1.20MB'
        1253656678 => '1.17GB'
    """
    factor = 1024
    for unit in ["", "K", "M", "G", "T", "P"]:
        if bytes < factor:
            return f"{bytes:.2f}{unit}{suffix}"
        bytes /= factor


def system_info():
    uname = platform.uname()
    cpufreq = psutil.cpu_freq()
    sys_info = ""
    sys_info += f"- Python version: {platform.python_version()}\n"
    sys_info += f"- Processor: {uname.processor}\n"
    sys_info += f"- Physical cores: {psutil.cpu_count(logical=False)}\n"
    sys_info += f"- Total cores: {psutil.cpu_count(logical=True)}\n"
    sys_info += f"- Max Frequency: {cpufreq.max:.2f}Mhz \n"
    sys_info += f"- Min Frequency: {cpufreq.min:.2f}Mhz\n"
    svmem = psutil.virtual_memory()
    sys_info += f"- Total Memory: {get_size(svmem.total)}\n"
    return sys_info


def versions_string():
    servers = {
        "Redis": kv_benchmark.Redis(redis.Redis(port=7379)),
        "Dragonfly": kv_benchmark.Redis(redis.Redis(port=10379)),
        "KeyDB": kv_benchmark.Redis(redis.Redis(port=11379)),
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
tmpl = tmpl.replace("{SYS_INFO}", system_info())
open("README.md", "w").write(tmpl)
