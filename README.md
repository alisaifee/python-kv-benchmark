# Key Value Store benchmarks with python client libraries

Benchmarks for some common operations with Memcached, Redis, Redis Cluster, Dragonfly, KeyDB, MongoDB and Etcd.

The benchmarks were run using [pytest-benchmark](https://pytest-benchmark.readthedocs.io/en/latest/) with the parameters:
- min_rounds=5
- min_time=0.000005
- max_time=1.0
- calibration_precision=10
- warmup=True
- warmup_iterations=100000

## Benchmark environment:
- Python version: 3.11.0
- Processor: x86_64
- Physical cores: 4
- Total cores: 8
- Max Frequency: 4200.00Mhz 
- Min Frequency: 800.00Mhz
- Total Memory: 31.23GB


## Server versions:
- Redis: 7.0.7
- Dragonfly: df-v0.13.1
- KeyDB: 6.3.1
- Memcached: 1.6.18
- Redis Cluster: 7.0.7
- MongoDB: 6.0.3
- Etcd: 3.5.6


## Python client libraries used:
- Redis/Redis Cluster/Dragonfly/KeyDB: [redis-py](https://github.com/redis/redis-py)
- Memcached: [pymemcache](https://github.com/pinterest/pymemcache)
- MongoDB: [pymongo](https://github.com/mongodb/mongo-python-driver)
- Etcd: [etcd3](https://github.com/kragniz/python-etcd3)

The associated implementations used in the benchmark can be found in [kv_benchmark.py](./kv_benchmark.py)

## Operations

### Get
- Redis/Redis Cluster/Dragonfly/KeyDB: [GET](https://redis.io/commands/get/)
- Memcached: [get](https://github.com/memcached/memcached/wiki/Commands#get)
- MongoDB: [findOne](https://www.mongodb.com/docs/manual/reference/method/db.collection.findOne/)
- Etcd: [get](https://python-etcd3.readthedocs.io/en/latest/usage.html#etcd3.Etcd3Client.get)

![get](./results/benchmark-get.svg)

### Set
- Redis/Redis Cluster/Dragonfly/KeyDB: [SET](https://redis.io/commands/set/)
- Memcached: [set](https://github.com/memcached/memcached/wiki/Commands#set)
- MongoDB: [replaceOne with upsert](https://www.mongodb.com/docs/manual/reference/method/db.collection.replaceOne/)
- Etcd: [put](https://python-etcd3.readthedocs.io/en/latest/usage.html#etcd3.Etcd3Client.put)

![set](./results/benchmark-set.svg)

### Increment
- Redis/Redis Cluster/Dragonfly/KeyDB: [INCRBY](https://redis.io/commands/incrby/)
- Memcached: [incr](https://github.com/memcached/memcached/wiki/Commands#incrdecr)
- MongoDB: [findOneAndUpdate with conditional $add and upsert](https://www.mongodb.com/docs/manual/reference/method/db.collection.findOneAndUpdate/)
- Etcd: [transaction with conditional put when key doesn't exist and get+local increment+put with another transaction with a CAS (in a loop) if it does](https://python-etcd3.readthedocs.io/en/latest/usage.html#etcd3.Etcd3Client.transactionhttps://python-etcd3.readthedocs.io/en/latest/usage.html#etcd3.Etcd3Client.transactionhttps://python-etcd3.readthedocs.io/en/latest/usage.html#etcd3.Etcd3Client.transactionhttps://python-etcd3.readthedocs.io/en/latest/usage.html#etcd3.Etcd3Client.transactionhttps://python-etcd3.readthedocs.io/en/latest/usage.html#etcd3.Etcd3Client.transactionhttps://python-etcd3.readthedocs.io/en/latest/usage.html#etcd3.Etcd3Client.transactionhttps://python-etcd3.readthedocs.io/en/latest/usage.html#etcd3.Etcd3Client.transactionhttps://python-etcd3.readthedocs.io/en/latest/usage.html#etcd3.Etcd3Client.transactionhttps://python-etcd3.readthedocs.io/en/latest/usage.html#etcd3.Etcd3Client.transaction)

![incr](./results/benchmark-incr.svg)

## Tabulated Results

```

----------------------------------------------- benchmark 'get': 7 tests -----------------------------------------------
Name (time in us)                Min                   Max                Mean            Rounds  OPS (Kops/s)          
------------------------------------------------------------------------------------------------------------------------
test_get[memcached]          45.7298 (1.0)        335.1234 (1.34)      68.8479 (1.0)       21313       14.5248 (1.0)    
test_get[redis]              59.4687 (1.30)       907.1268 (3.61)      86.9582 (1.26)      16708       11.4998 (0.79)   
test_get[redis-cluster]      60.3814 (1.32)     1,075.5714 (4.29)      82.1646 (1.19)      16314       12.1707 (0.84)   
test_get[keydb]              65.2242 (1.43)       250.9858 (1.0)      103.8087 (1.51)      15276        9.6331 (0.66)   
test_get[dragonfly]          73.3994 (1.61)     1,323.9216 (5.27)     112.6412 (1.64)      12896        8.8777 (0.61)   
test_get[etcd]              232.2756 (5.08)     1,244.9622 (4.96)     355.7405 (5.17)       4323        2.8110 (0.19)   
test_get[mongodb]           263.9126 (5.77)       637.9038 (2.54)     419.4586 (6.09)       3690        2.3840 (0.16)   
------------------------------------------------------------------------------------------------------------------------

------------------------------------------------- benchmark 'incr': 7 tests -------------------------------------------------
Name (time in us)                   Min                    Max                  Mean            Rounds          OPS          
-----------------------------------------------------------------------------------------------------------------------------
test_incr[memcached]            41.4997 (1.0)         341.0205 (1.31)        60.1032 (1.0)       24386  16,638.0513 (1.0)    
test_incr[redis]                62.3912 (1.50)        275.1127 (1.06)        99.7772 (1.66)      16017  10,022.3288 (0.60)   
test_incr[keydb]                67.7779 (1.63)        260.4481 (1.0)        106.4859 (1.77)      13974   9,390.9162 (0.56)   
test_incr[redis-cluster]        71.9111 (1.73)        283.5412 (1.09)       110.2970 (1.84)      13861   9,066.4258 (0.54)   
test_incr[dragonfly]            77.3557 (1.86)      1,100.2291 (4.22)       114.2064 (1.90)      12308   8,756.0761 (0.53)   
test_incr[mongodb]             318.5272 (7.68)        712.7319 (2.74)       473.5727 (7.88)       2927   2,111.6081 (0.13)   
test_incr[etcd]              3,660.7757 (88.21)    17,379.6639 (66.73)    5,934.5825 (98.74)       397     168.5039 (0.01)   
-----------------------------------------------------------------------------------------------------------------------------

------------------------------------------------- benchmark 'set': 7 tests -------------------------------------------------
Name (time in us)                  Min                   Max                  Mean            Rounds           OPS          
----------------------------------------------------------------------------------------------------------------------------
test_set[memcached]             4.3651 (1.0)         64.9439 (1.0)          5.0364 (1.0)      113962  198,554.2481 (1.0)    
test_set[redis]                63.7732 (14.61)    1,563.7595 (24.08)       98.7082 (19.60)     15571   10,130.8660 (0.05)   
test_set[keydb]                69.9200 (16.02)      435.7602 (6.71)       105.2783 (20.90)     14201    9,498.6322 (0.05)   
test_set[redis-cluster]        74.1240 (16.98)    7,578.7418 (116.70)     121.1131 (24.05)     13762    8,256.7424 (0.04)   
test_set[dragonfly]            82.2525 (18.84)    6,701.1714 (103.18)     121.0336 (24.03)     11686    8,262.1673 (0.04)   
test_set[mongodb]           2,189.9920 (501.70)   6,739.1917 (103.77)   2,981.4995 (591.99)     2939      335.4017 (0.00)   
test_set[etcd]              2,196.1033 (503.10)   8,621.7523 (132.76)   2,744.9254 (545.02)      768      364.3086 (0.00)   
----------------------------------------------------------------------------------------------------------------------------

Legend:
  Outliers: 1 Standard Deviation from Mean; 1.5 IQR (InterQuartile Range) from 1st Quartile and 3rd Quartile.
  OPS: Operations Per Second, computed as 1 / Mean

```

## Development

To run these benchmarks locally you'll need a working docker & docker-compose installation.

1. Install the requirements: `pip install --no-binary=protobuf requirements.txt`
2. Run the benchmarks: `make generate` (this task will also update the report in this README)
3. Or, run the benchmarks directly: `pytest`

