import json
from emails import send_email


def decode_json(line):
    return json.loads(line)


class Log:
    def __init__(self, name, codec=decode_json):
        self.name = name
        self.codec = codec
        self.fns = set()

    def decode(self, line):
        return self.codec(line)

    def process(self, line):
        entry = self.decode(line)
        for fn in self.fns:
            try:
                yield from fn(entry, self.name)
            except Exception as e:
                send_email(fn.owners, e)

    def register(self, fn):
        self.fns.add(fn)
        return fn

    def __str__(self):
        res = [self.name]
        for f in self.fns:
            res.append(f"\t{f.__name__}")
            res.append("\t\t" + " ".join(f.owners))
        return "\n".join(res)
