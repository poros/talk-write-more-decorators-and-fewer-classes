from .logs import events
from statmonster import owners, register, Counter


@register(events)
@owners("antonio@yelp.com")
def count_events(entry, log):
    yield Counter("events", entry["time"], 1, {"type": entry["type"]})
