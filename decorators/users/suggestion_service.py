from statmonster import owners
from logs import suggestions_service
from .service import emit_service_timings, emit_service_counters


@suggestions_service.register
@owners("search@yelp.com")
def emit_suggestions_metrics(entry):
    yield from emit_service_timings("suggestion_timings", entry)
    yield from emit_service_counters("suggestion_count", entry)
