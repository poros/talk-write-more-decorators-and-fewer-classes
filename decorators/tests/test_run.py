from statmonster import MetricType
from collect import collect

def test_run():
    logs = dict(collect())
    line = '{"time": 123456, "time_elapsed": 12, "status": 200, "method_name": "GET", "blob": "foo"}'
    metrics = list(logs['suggestions_service'].process(line))
    assert len(metrics) == 3
    assert sum(1 for m in metrics if m.type == MetricType.COUNTER) == 2
    assert sum(1 for m in metrics if m.type == MetricType.TIMER) == 1
