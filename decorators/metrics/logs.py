from statmonster import Log
from utils import decode_apache
from functools import partial


events = Log("events")
rusage = Log("rusage")
suggestions_service = Log("suggest")
home = Log("homepage")


ApacheLog = partial(Log, codec=decode_apache)
access = ApacheLog("access")
admin_access = ApacheLog("admin_access")


def decode_text(line):
    time, request = line.split()
    return {'time': time, 'request': request}


requests = Log("tmp_requests", codec=decode_text)
