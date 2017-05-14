from statmonster import Log
from ._endpoints import EndpointsTimingBaseTrigger


class HomePageLog(Log):
    name = "homepage"


class HomePageEndpointsTrigger(EndpointsTimingBaseTrigger):
    owners = ["consumer@yelp.com"]
    endpoints = ["best_of_yelp", "suggestions", "nearby"]
    metrics_name = "home"

    def get_additional_dimensions(self, entry):
        return {
            "mode": entry.get("mode", "sync"),
            "user": "loggedin" if entry["username"] else "anonymous",
        }
