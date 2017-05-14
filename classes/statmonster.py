from log import Log  # noqa
from trigger import Trigger  # noqa
from collections import namedtuple
from functools import partial
from emails import send_email


Metric = namedtuple("Metric", ("name", "ts", "value", "dims", "type"))
Counter = partial(Metric, type="C")
Timer = partial(Metric, type="T")


def process(log, triggers, line):
    entry = log.decode(line)
    for trigger in triggers:
        try:
            yield from trigger.digest(entry, log.name)
        except Exception as e:
            send_email(trigger.owners, e)
