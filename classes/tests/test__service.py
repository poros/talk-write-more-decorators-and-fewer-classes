import pytest
from ._service import ServiceCountBaseTrigger
from statmonter import Counter


class TestServiceCountBaseTrigger():
	@pytest.fixture
	def trigger(self):
		return type(
			'TestTrigger',
			(ServiceCountBaseTrigger,),
			{'metric_name': 'TestCount', "owners": ["foo@yelp.com"]},
		)()

	def test_digest(self, trigger):
		entry = {
			'time': 123456,
			'status': 200,
			'blob': 'bla',
		}
		expected = [Counter(('TestCount',), 123456, 1, {'status': 200})]
		assert list(trigger.digest(entry)) == expected
