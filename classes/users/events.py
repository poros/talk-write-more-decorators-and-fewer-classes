from statmonster import Log, Trigger, Counter


class EventsLog(Log):
    name = "events"


class CountEventsTrigger(Trigger):
    owners = ["antonio@yelp.com"]

    def digest(entry, log):
        yield Counter("events", entry["time"], 1, {"type": entry["type"]})
