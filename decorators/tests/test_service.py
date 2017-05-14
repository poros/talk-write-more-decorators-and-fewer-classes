from users.service import emit_service_counters
from statmonster import Counter


def test_emit_service_counters():
    entry = {
        "time": 123456,
        "status": 200,
        "method_name": "GET",
        "blob": "foo",
    }
    expected = Counter("test.request_count", 123456, 1, {"method": "GET"})
    assert expected in list(emit_service_counters("test", entry))
