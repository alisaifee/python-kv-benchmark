# Key Value Store benchmarks with python client libraries

Benchmarks for some common operations with Memcached, Redis, Redis Cluster, Dragonfly, MongoDB and Etcd.

Server versions:
- Redis: 6.2.6
- Dragonfly: df--128-NOTFOUND
- Memcached: 1.6.17
- Redis Cluster: 6.2.6
- MongoDB: 6.0.3
- Etcd: 3.5.6


Python client libraries used:
- Redis: [redis-py](https://github.com/redis/redis-py)
- Memcached: [pymemcache](https://github.com/pinterest/pymemcache)
- MongoDB: [pymongo](https://github.com/mongodb/mongo-python-driver)
- Etcd: [etcd3](https://github.com/kragniz/python-etcd3)

The associated wrappers used in the benchmark can be found in [kv_benchmark.py](./kv_benchmark.py)

## Get
![get](./results/benchmark-get.svg)

## Set
![set](./results/benchmark-set.svg)

## Atomic Increment
![set](./results/benchmark-incr.svg)

## Tabulated Results

```

----------------------------------------------- benchmark 'get': 6 tests -----------------------------------------------
Name (time in us)                Min                   Max                Mean            Rounds  OPS (Kops/s)
------------------------------------------------------------------------------------------------------------------------
test_get[memcached]          46.5252 (1.0)        505.3710 (1.86)      71.3497 (1.0)       21303       14.0155 (1.0)
test_get[redis]              62.2533 (1.34)       271.8531 (1.0)       99.2341 (1.39)      15962       10.0772 (0.72)
test_get[redis-cluster]      66.9714 (1.44)     8,420.1917 (30.97)     83.1509 (1.17)      14954       12.0263 (0.86)
test_get[dragonfly]          80.2130 (1.72)     2,529.5001 (9.30)     121.4603 (1.70)      12986        8.2331 (0.59)
test_get[etcd]              270.4915 (5.81)     1,447.5789 (5.32)     401.0804 (5.62)       3542        2.4933 (0.18)
test_get[mongodb]           336.6992 (7.24)       691.4064 (2.54)     494.5290 (6.93)       2821        2.0221 (0.14)
------------------------------------------------------------------------------------------------------------------------

------------------------------------------------- benchmark 'incr': 6 tests -------------------------------------------------
Name (time in us)                   Min                    Max                  Mean            Rounds          OPS
-----------------------------------------------------------------------------------------------------------------------------
test_incr[memcached]            42.3566 (1.0)         379.4096 (1.41)        62.2827 (1.0)       23567  16,055.8281 (1.0)
test_incr[redis]                65.6415 (1.55)        269.7017 (1.0)        112.0891 (1.80)      15171   8,921.4735 (0.56)
test_incr[dragonfly]            76.6050 (1.81)      2,933.3252 (10.88)      118.5074 (1.90)      13647   8,438.2924 (0.53)
test_incr[redis-cluster]        80.8556 (1.91)        278.4468 (1.03)       123.6346 (1.99)      12526   8,088.3495 (0.50)
test_incr[mongodb]             367.7029 (8.68)        739.2839 (2.74)       527.7318 (8.47)       2542   1,894.9020 (0.12)
test_incr[etcd]              3,219.4164 (76.01)    11,079.2238 (41.08)    4,235.2141 (68.00)       427     236.1156 (0.01)
-----------------------------------------------------------------------------------------------------------------------------

------------------------------------------------- benchmark 'set': 6 tests -------------------------------------------------
Name (time in us)                  Min                   Max                  Mean            Rounds           OPS
----------------------------------------------------------------------------------------------------------------------------
test_set[memcached]             5.7276 (1.0)        102.0078 (1.0)          7.1655 (1.0)      174763  139,556.8138 (1.0)
test_set[redis]                67.6401 (11.81)      245.3141 (2.40)        99.8682 (13.94)     14729   10,013.1992 (0.07)
test_set[dragonfly]            77.4171 (13.52)    3,711.1640 (36.38)      130.0071 (18.14)     12919    7,691.8900 (0.06)
test_set[redis-cluster]        81.2169 (14.18)      430.3195 (4.22)       131.2064 (18.31)     12202    7,621.5796 (0.05)
test_set[etcd]              1,488.9613 (259.96)   8,214.0695 (80.52)    2,235.9053 (312.04)     1078      447.2461 (0.00)
test_set[mongodb]           1,923.8200 (335.88)   4,982.9073 (48.85)    2,656.4706 (370.73)     2346      376.4393 (0.00)
----------------------------------------------------------------------------------------------------------------------------

Legend:
  Outliers: 1 Standard Deviation from Mean; 1.5 IQR (InterQuartile Range) from 1st Quartile and 3rd Quartile.
  OPS: Operations Per Second, computed as 1 / Mean

```
