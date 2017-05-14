from .logs import home
from .endpoints import emit_endpoints_timings
from statmonster import owners, register


ENDPOINTS = ["best_of_yelp", "suggestions", "nearby"]

@register(home)
@owners("consumer@yelp.com")
def time_home_endpoints(entry):
    dims = {
        "mode": entry.get("mode", "sync"),
        "user": "loggedin" if entry["username"] else "anonymous",
    }
    return emit_endpoints_timings("home", ENDPOINTS, dims, entry)
