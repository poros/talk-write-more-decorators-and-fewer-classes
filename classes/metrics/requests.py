from statmonster import Log


def decode_text(line):
    time, request = line.split()
    return {'time': time, 'request': request}


class RequestsLog(Log):
    name = "tmp_requests"
    decoder = decode_text
