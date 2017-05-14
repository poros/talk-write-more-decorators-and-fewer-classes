from .logs import rusage
from statmonster import owners, Timer


@rusage.register
@owners("antonio@yelp.com", "metrics@yelp.com")
def time_cpu(entry):
    for metric in ("stime", "utime"):
        yield Timer(f"cpu.{metric}", entry["start_time"], entry[metric], {})
