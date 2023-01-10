import uuid

import pytest

from tests.fixtures import all_storage


@all_storage
@pytest.mark.benchmark(group="get")
def test_get(fixture, benchmark):
    benchmark(fixture.get, "fubar")


@all_storage
@pytest.mark.benchmark(group="set")
def test_set(fixture, benchmark):
    uid = uuid.uuid4().hex
    benchmark(fixture.set, uid, "fubar")


@all_storage
@pytest.mark.benchmark(group="incr")
def test_incr(fixture, benchmark):
    benchmark(fixture.incr, "fubar")
