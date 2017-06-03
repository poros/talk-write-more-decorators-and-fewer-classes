from statmonster import MetricType, process
from collect import collect

def test_run():
    log, triggers = [(l, t) for l, t in collect().items() if l.name == "suggest"][0]
    line = '{"time": 123456, "time_elapsed": 12, "status": 200, "method_name": "GET", "blob": "foo"}'
    metrics = list(process(log, triggers, line))
    assert len(metrics) == 3
    assert sum(1 for m in metrics if m.type == MetricType.COUNTER) == 2
    assert sum(1 for m in metrics if m.type == MetricType.TIMER) == 1
