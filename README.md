# Key Value Store benchmarks with python client libraries

Benchmarks for some common operations with Memcached, Redis, Redis Cluster, Dragonfly, MongoDB and Etcd.

The benchmarks were run using [pytest-benchmark](https://pytest-benchmark.readthedocs.io/en/latest/) with the parameters:
- min_rounds=5
- min_time=0.000005
- max_time=1.0
- calibration_precision=10
- warmup=True
- warmup_iterations=100000

## Server versions:
- Redis: 7.0.7
- Dragonfly: df-v0.13.1
- Memcached: 1.6.18
- Redis Cluster: 7.0.7
- MongoDB: 6.0.3
- Etcd: 3.5.6


## Python client libraries used:
- Redis: [redis-py](https://github.com/redis/redis-py)
- Memcached: [pymemcache](https://github.com/pinterest/pymemcache)
- MongoDB: [pymongo](https://github.com/mongodb/mongo-python-driver)
- Etcd: [etcd3](https://github.com/kragniz/python-etcd3)

The associated wrappers used in the benchmark can be found in [kv_benchmark.py](./kv_benchmark.py)

## Operations

### Get
- Redis: [GET](https://redis.io/commands/get/)
- Memcached: [get](https://github.com/memcached/memcached/wiki/Commands#get)
- MongoDB: [findOne](https://www.mongodb.com/docs/manual/reference/method/db.collection.findOne/)
- Etcd: [get](https://python-etcd3.readthedocs.io/en/latest/usage.html#etcd3.Etcd3Client.get)

![get](./results/benchmark-get.svg)

### Set
- Redis: [SET](https://redis.io/commands/set/)
- Memcached: [set](https://github.com/memcached/memcached/wiki/Commands#set)
- MongoDB: [replaceOne with upsert](https://www.mongodb.com/docs/manual/reference/method/db.collection.replaceOne/)
- Etcd: [put](https://python-etcd3.readthedocs.io/en/latest/usage.html#etcd3.Etcd3Client.put)

![set](./results/benchmark-set.svg)

### Increment
- Redis: [INCRBY](https://redis.io/commands/incrby/)
- Memcached: [incr](https://github.com/memcached/memcached/wiki/Commands#incrdecr)
- MongoDB: [findOneAndUpdate with conditional $add and upsert](https://www.mongodb.com/docs/manual/reference/method/db.collection.findOneAndUpdate/)
- Etcd: [transaction with conditional put when key doesn't exist and get+local increment+put with another transaction with a CAS (in a loop) if it does](https://python-etcd3.readthedocs.io/en/latest/usage.html#etcd3.Etcd3Client.transactionhttps://python-etcd3.readthedocs.io/en/latest/usage.html#etcd3.Etcd3Client.transactionhttps://python-etcd3.readthedocs.io/en/latest/usage.html#etcd3.Etcd3Client.transactionhttps://python-etcd3.readthedocs.io/en/latest/usage.html#etcd3.Etcd3Client.transactionhttps://python-etcd3.readthedocs.io/en/latest/usage.html#etcd3.Etcd3Client.transactionhttps://python-etcd3.readthedocs.io/en/latest/usage.html#etcd3.Etcd3Client.transactionhttps://python-etcd3.readthedocs.io/en/latest/usage.html#etcd3.Etcd3Client.transactionhttps://python-etcd3.readthedocs.io/en/latest/usage.html#etcd3.Etcd3Client.transactionhttps://python-etcd3.readthedocs.io/en/latest/usage.html#etcd3.Etcd3Client.transaction)

![incr](./results/benchmark-incr.svg)

## Tabulated Results

```

----------------------------------------------- benchmark 'get': 6 tests -----------------------------------------------
Name (time in us)                Min                   Max                Mean            Rounds  OPS (Kops/s)
------------------------------------------------------------------------------------------------------------------------
test_get[memcached]          46.2886 (1.0)        239.0742 (1.0)       67.3889 (1.0)       21306       14.8392 (1.0)
test_get[redis]              63.4044 (1.37)       655.9808 (2.74)      94.9694 (1.41)      15703       10.5297 (0.71)
test_get[redis-cluster]      68.1840 (1.47)     3,178.0265 (13.29)     86.7683 (1.29)      14491       11.5249 (0.78)
test_get[dragonfly]          78.4546 (1.69)     2,581.0115 (10.80)    107.8804 (1.60)      12381        9.2695 (0.62)
test_get[etcd]              258.9356 (5.59)     1,405.9283 (5.88)     374.7329 (5.56)       3862        2.6686 (0.18)
test_get[mongodb]           333.5532 (7.21)       652.3281 (2.73)     450.9450 (6.69)       3155        2.2176 (0.15)
------------------------------------------------------------------------------------------------------------------------

------------------------------------------------- benchmark 'incr': 6 tests -------------------------------------------------
Name (time in us)                   Min                    Max                  Mean            Rounds          OPS
-----------------------------------------------------------------------------------------------------------------------------
test_incr[memcached]            41.9859 (1.0)         289.7419 (1.33)        60.2492 (1.0)       23763  16,597.7211 (1.0)
test_incr[redis]                65.6173 (1.56)        808.6655 (3.72)        94.0280 (1.56)      15262  10,635.1295 (0.64)
test_incr[redis-cluster]        79.7976 (1.90)        217.1081 (1.0)        112.3889 (1.87)      12378   8,897.6722 (0.54)
test_incr[dragonfly]            85.0763 (2.03)        402.8399 (1.86)       125.0318 (2.08)      13802   7,997.9671 (0.48)
test_incr[mongodb]             354.7017 (8.45)      2,750.7134 (12.67)      510.0775 (8.47)       2775   1,960.4863 (0.12)
test_incr[etcd]              3,637.1667 (86.63)    17,569.4879 (80.93)    4,805.7060 (79.76)       432     208.0860 (0.01)
-----------------------------------------------------------------------------------------------------------------------------

-------------------------------------------------- benchmark 'set': 6 tests -------------------------------------------------
Name (time in us)                  Min                    Max                  Mean            Rounds           OPS
-----------------------------------------------------------------------------------------------------------------------------
test_set[memcached]             5.6587 (1.0)          95.6319 (1.0)          6.5051 (1.0)      174820  153,725.5402 (1.0)
test_set[redis]                67.5637 (11.94)       286.0725 (2.99)       102.0467 (15.69)     14524    9,799.4380 (0.06)
test_set[redis-cluster]        81.2504 (14.36)       660.3338 (6.90)       125.9659 (19.36)     12358    7,938.6591 (0.05)
test_set[dragonfly]            85.0838 (15.04)       256.2199 (2.68)       114.2516 (17.56)     11861    8,752.6147 (0.06)
test_set[etcd]              1,062.7694 (187.81)   11,504.8140 (120.30)   2,681.3506 (412.19)      970      372.9464 (0.00)
test_set[mongodb]           1,918.8132 (339.09)    5,205.2159 (54.43)    2,565.2069 (394.34)     2225      389.8321 (0.00)
-----------------------------------------------------------------------------------------------------------------------------

Legend:
  Outliers: 1 Standard Deviation from Mean; 1.5 IQR (InterQuartile Range) from 1st Quartile and 3rd Quartile.
  OPS: Operations Per Second, computed as 1 / Mean

```
