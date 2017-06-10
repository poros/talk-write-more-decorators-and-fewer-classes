from statmonster import Counter


def emit_endpoints_timings(metric_name, endpoints, additional_dims, entry):
    ts = entry['start_time']
    for endpoint in endpoints:
        if endpoint == entry["endpoint"]:
            timing = entry["endpoint"]["time"]
            dims = {'endpoint': endpoint}.update(additional_dims)
            yield Counter(metric_name, ts, timing, dims)
