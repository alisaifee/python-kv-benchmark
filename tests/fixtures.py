import pytest

all_storage = pytest.mark.parametrize(
    "fixture",
    [
        pytest.param(
            pytest.lazy_fixture("redis"),
            marks=pytest.mark.redis,
            id="redis",
        ),
        pytest.param(
            pytest.lazy_fixture("memcached"),
            marks=pytest.mark.memcached,
            id="memcached",
        ),
        pytest.param(
            pytest.lazy_fixture("redis_cluster"),
            marks=pytest.mark.redis_cluster,
            id="redis-cluster",
        ),
        pytest.param(
            pytest.lazy_fixture("mongodb"),
            marks=pytest.mark.mongodb,
            id="mongodb",
        ),
        pytest.param(
            pytest.lazy_fixture("etcd"),
            marks=pytest.mark.etcd,
            id="etcd",
        ),
        pytest.param(
            pytest.lazy_fixture("dragonfly"),
            marks=pytest.mark.dragonfly,
            id="dragonfly",
        ),
    ],
)
