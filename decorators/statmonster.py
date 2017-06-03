from enum import Enum
from log import Log  # noqa
from collections import namedtuple
from functools import partial

MetricType = Enum("MetricsType", ("Counter", "Timer"))
Metric = namedtuple("Metric", ("name", "ts", "value", "dims", "type"))
Counter = partial(Metric, type=MetricType.Counter)
Timer = partial(Metric, type=MetricType.Timer)


def owners(*handlers):
    def decorator(fn):
        fn.owners = handlers
        return fn

    return decorator


def register(*logs):
    def decorator(fn):
        for log in logs:
            log.register(fn)
        return fn

    return decorator
