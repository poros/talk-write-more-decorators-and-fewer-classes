import json


def decode_json(line):
    return json.loads(line)


class Log:
    codec = decode_json

    def __init__(self):
        assert self.name, "log name must be specified"

    @classmethod
    def decode(cls, line):
        return cls.codec(line)

    def __str__(self):
        return self.name
