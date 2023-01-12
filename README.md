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
test_get[memcached]          45.7466 (1.0)        330.8877 (1.46)      71.3854 (1.0)       21758       14.0085 (1.0)    
test_get[redis]              61.5176 (1.34)       226.1493 (1.0)       90.7892 (1.27)      16184       11.0145 (0.79)   
test_get[redis-cluster]      61.6200 (1.35)     3,291.7839 (14.56)     91.9745 (1.29)      16377       10.8726 (0.78)   
test_get[keydb]              66.9099 (1.46)       365.4733 (1.62)     102.4025 (1.43)      14890        9.7654 (0.70)   
test_get[dragonfly]          80.2614 (1.75)     3,998.8700 (17.68)    111.9683 (1.57)      12657        8.9311 (0.64)   
test_get[etcd]              236.5839 (5.17)     1,290.8094 (5.71)     353.4472 (4.95)       4181        2.8293 (0.20)   
test_get[mongodb]           276.9809 (6.05)       909.8575 (4.02)     428.7571 (6.01)       3352        2.3323 (0.17)   
------------------------------------------------------------------------------------------------------------------------

------------------------------------------------- benchmark 'incr': 7 tests -------------------------------------------------
Name (time in us)                   Min                    Max                  Mean            Rounds          OPS          
-----------------------------------------------------------------------------------------------------------------------------
test_incr[memcached]            40.8143 (1.0)         269.8805 (1.09)        59.5558 (1.0)       24367  16,790.9848 (1.0)    
test_incr[redis]                63.1604 (1.55)        263.5680 (1.07)        95.0791 (1.60)      15832  10,517.5553 (0.63)   
test_incr[keydb]                69.5381 (1.70)        782.0800 (3.17)       107.4456 (1.80)      13895   9,307.0367 (0.55)   
test_incr[redis-cluster]        72.6990 (1.78)        246.6347 (1.0)        119.9712 (2.01)      13831   8,335.3314 (0.50)   
test_incr[dragonfly]            79.4530 (1.95)        679.2080 (2.75)       114.1991 (1.92)      12104   8,756.6383 (0.52)   
test_incr[mongodb]             314.2320 (7.70)        743.1395 (3.01)       477.6460 (8.02)       2976   2,093.6007 (0.12)   
test_incr[etcd]              3,545.9250 (86.88)    13,843.9164 (56.13)    5,744.0997 (96.45)       322     174.0917 (0.01)   
-----------------------------------------------------------------------------------------------------------------------------

-------------------------------------------------- benchmark 'set': 7 tests -------------------------------------------------
Name (time in us)                  Min                    Max                  Mean            Rounds           OPS          
-----------------------------------------------------------------------------------------------------------------------------
test_set[memcached]             4.2738 (1.0)          49.8956 (1.0)          5.0813 (1.0)      114155  196,798.5778 (1.0)    
test_set[redis]                65.2932 (15.28)       284.6308 (5.70)        97.6322 (19.21)     15413   10,242.5273 (0.05)   
test_set[keydb]                70.7246 (16.55)       971.8258 (19.48)      110.5350 (21.75)     14020    9,046.9068 (0.05)   
test_set[redis-cluster]        73.4366 (17.18)       236.5578 (4.74)       116.9449 (23.01)     13690    8,551.0325 (0.04)   
test_set[dragonfly]            85.4265 (19.99)       350.8665 (7.03)       122.1020 (24.03)     11842    8,189.8720 (0.04)   
test_set[etcd]                913.2028 (213.67)    8,495.3923 (170.26)   2,282.7113 (449.23)     1088      438.0756 (0.00)   
test_set[mongodb]           2,174.3532 (508.76)   12,633.6832 (253.20)   2,949.7241 (580.50)     2892      339.0148 (0.00)   
-----------------------------------------------------------------------------------------------------------------------------

Legend:
  Outliers: 1 Standard Deviation from Mean; 1.5 IQR (InterQuartile Range) from 1st Quartile and 3rd Quartile.
  OPS: Operations Per Second, computed as 1 / Mean

```

## Development

To run these benchmarks locally you'll need a working docker & docker-compose installation.

1. Install the requirements: `pip install --no-binary=protobuf requirements.txt`
2. Run the benchmarks: `make generate` (this task will also update the report in this README)
3. Or, run the benchmarks directly: `pytest`

