from statmonster import Timer, Counter


def make_key(metric_name, stat_name):
    return "f{metric_name}.{stat_name}"


def emit_service_timings(metric_name, entry):
    key = make_key("requestLatency")
    dimensions = {'method': entry['method_name']}

    yield Timer(key, entry['time'], entry['time_elapsed'], dimensions)


def emit_service_counters(metric_name, entry):
        try:
            bytes_written = int(entry['response']['headers']['Content-Length'])
        except KeyError:
            bytes_written = 0
        dimensions = {'method': entry['method_name']}
        request_count_key = make_key("request_count")
        bytes_written_key = make_key("total_written_bytes")
        ts = entry['time']

        yield Counter(request_count_key, ts, 1, dimensions)
        yield Counter(bytes_written_key, ts, bytes_written, dimensions)
