from statmonster import Trigger, Counter

class EndpointsTimingBaseTrigger(Trigger):
    metric_name = None
    endpoints = None

    def __init__(self):
        super().__init__()
        assert self.metric_name
        assert self.endpoints

    def get_additional_dimensions(self, entry):
        return {}

    def digest(self, entry):
        ts = entry['start_time']
        add_dims = self.get_additional_dimensions(entry)
        for endpoint in self.endpoints:
            if endpoint == entry["endpoint"]:
                timing = entry["endpoint"]["time"]
                dims = {'endpoint': endpoint}.update(add_dims)
                yield Counter(self.metric_name, ts, timing, dims)
