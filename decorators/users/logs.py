from statmonster import Log
from decoders import decode_apache
from functool import partial


events = Log("events")
searches = Log("tmp_searches")


ApacheLog = partial(Log, codec=decode_apache)
access = ApacheLog("access")
admin_access = ApacheLog("admin_access")


def decode_text(line):
    time, request = line.split()
    return {'time': time, 'request': request}


requests = Log("tmp_requests", codec=decode_text)