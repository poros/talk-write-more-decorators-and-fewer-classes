class Trigger:
    owners = None

    def __init__(self):
        assert self.owners

    def digest(self, line):
        raise NotImplementedError
