from statmonster import Log, Trigger, Timer


class RusageLog(Log):
    name = "rusage"


class TimeCpuTrigger(Trigger):
    owners = ["antonio@yelp.com", "metrics@yelp.com"]

    def digest(self, entry, log):
        for metric in ("stime", "utime"):
            yield Timer(f"cpu.{metric}", entry["start_time"], entry[metric], {})
