import json


def decode_json(line):
    return json.loads(line)


class Log:
    def __init__(self, name, codec=decode_json):
        self.name = name
        self.codec = codec

    def decode(self, line):
        return self.codec(line)
