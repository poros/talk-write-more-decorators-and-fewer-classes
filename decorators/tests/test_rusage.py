from users.rusage import time_cpu
from statmonster import Timer


def test_time_cpu():
    entry = {"time": 1000, "stime": 42, "ctime": 33}
    assert Timer("cpu.stime", 1000, 42, {}) in list(time_cpu(entry, "foo"))
