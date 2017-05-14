from collect import collect

def test_owners():
    for name, log in collect():
        for fn in log.fns:
            assert hasattr(fn, "owners")
