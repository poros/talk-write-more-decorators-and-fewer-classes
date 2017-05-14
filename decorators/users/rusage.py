from .logs import rusage
from statmonster import owners, Timer


@rusage.register
@owners("antonio@yelp.com", "metrics@yelp.com")
def time_cpu(entry, log):
    yield Timer("cpu.stime", entry["time"], entry["stime"], {})
