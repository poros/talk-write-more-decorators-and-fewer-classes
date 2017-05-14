from users.rusage import time_cpu
from statmonster import Timer


def test_time_cpu():
    entry = {"start_time": 1000, "stime": 42, "utime": 33}
    assert Timer("cpu.stime", 1000, 42, {}) in list(time_cpu(entry))
