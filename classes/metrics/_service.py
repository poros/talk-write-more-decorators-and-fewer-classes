from statmonster import Trigger, Timer, Counter


class ServiceBaseTrigger(Trigger):
    def __init__(self):
        super().__init__()
        assert self.metric_name

    def make_key(self, stat_name):
        return f"{self.metric_name}.{stat_name}"


class ServiceTimingBaseTrigger(ServiceBaseTrigger):

    def digest(self, entry):
        key = self.make_key("request_latency")
        dimensions = {'method': entry['method_name']}

        yield Timer(key, entry['time'], entry['time_elapsed'], dimensions)


class ServiceCountBaseTrigger(ServiceBaseTrigger):

    def digest(self, entry):
        try:
            bytes_written = int(entry['response']['headers']['Content-Length'])
        except KeyError:
            bytes_written = 0
        dimensions = {'method': entry['method_name']}
        request_count_key = self.make_key("request_count")
        bytes_written_key = self.make_key("total_written_bytes")
        ts = entry['time']

        yield Counter(request_count_key, ts, 1, dimensions)
        yield Counter(bytes_written_key, ts, bytes_written, dimensions)
