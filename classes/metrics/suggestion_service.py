from statmonster import Log
from ._service import ServiceTimingBaseTrigger, ServiceCountBaseTrigger


class SuggestionsLog(Log):
    name = "suggest"


class SuggestionsTimings(ServiceTimingBaseTrigger):
    owners = ["search@yelp.com"]
    metric_name = 'suggestions_timings'


class SuggestionsCount(ServiceCountBaseTrigger):
    owners = ["search@yelp.com"]
    metric_name = 'suggestions_count'
