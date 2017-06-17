import pytest
from metrics._service import ServiceCountBaseTrigger
from statmonster import Counter


@pytest.fixture
def trigger(self):
    return type(
        "TestTrigger",
        (ServiceCountBaseTrigger,),
        {"metric_name": "test", "owners": ["foo@yelp.com"]},
    )()


def test_digest(self, trigger):
    entry = {
        "time": 123456,
        "status": 200,
        "method_name": "GET",
        "blob": "bla",
    }
    expected = Counter("test.request_count", 123456, 1, {"method": "GET"})
    assert expected in list(trigger.digest(entry))
