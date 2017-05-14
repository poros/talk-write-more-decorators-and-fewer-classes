from log import Log  # noqa
from collections import namedtuple
from functools import partial


Metric = namedtuple("Metric", ("name", "ts", "value", "dims", "type"))
Counter = partial(Metric, type="C")
Timer = partial(Metric, type="T")


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
