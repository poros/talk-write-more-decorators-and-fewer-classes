class Trigger:
    def __init__(self):
        assert self.owners

    def digest(self, line):
        raise NotImplementedError
