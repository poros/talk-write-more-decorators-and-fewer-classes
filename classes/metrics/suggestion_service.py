from statmonster import Log
from ._service import ServiceTimingBaseTrigger, ServiceCountBaseTrigger


class SuggestionsLog(Log):
    name = "suggest"


class SuggestionsStatsTimings(ServiceTimingBaseTrigger):
    owners = ["search@yelp.com"]
    metric_name = 'suggestions_timings'


class SuggestionsStatsCount(ServiceCountBaseTrigger):
    owners = ["search@yelp.com"]
    metric_name = 'suggestions_count'
