import pytest
from pytest_lazy_fixtures import lf

all_storage = pytest.mark.parametrize(
    "fixture",
    [
        pytest.param(
            lf("redis"),
            marks=pytest.mark.redis,
            id="redis",
        ),
        pytest.param(
            lf("memcached"),
            marks=pytest.mark.memcached,
            id="memcached",
        ),
        pytest.param(
            lf("redis_cluster"),
            marks=pytest.mark.redis_cluster,
            id="redis-cluster",
        ),
        pytest.param(
            lf("mongodb"),
            marks=pytest.mark.mongodb,
            id="mongodb",
        ),
        pytest.param(
            lf("etcd"),
            marks=pytest.mark.etcd,
            id="etcd",
        ),
        pytest.param(
            lf("dragonfly"),
            marks=pytest.mark.dragonfly,
            id="dragonfly",
        ),
        pytest.param(
            lf("keydb"),
            marks=pytest.mark.keydb,
            id="keydb",
        ),
    ],
)
