from .service import emit_service_counters
from statmonter import Counter


def test_emit_service_counters():
    entry = {
        'time': 123456,
        'status': 200,
        'blob': 'bla',
    }
    expected = Counter("test_count", 123456, 1, {'status': 200})
    assert expected in list(emit_service_counters("test_count", entry))
