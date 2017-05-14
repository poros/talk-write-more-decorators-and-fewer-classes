from users.rusage import TimeCpuTrigger
from statmonster import Timer
import pytest


@pytest.fixture
def trigger():
    return TimeCpuTrigger()


def test_time_cpu(trigger):
    entry = {"start_time": 1000, "stime": 42, "utime": 33}
    assert Timer("cpu.stime", 1000, 42, {}) in list(trigger.digest(entry, "foo"))
