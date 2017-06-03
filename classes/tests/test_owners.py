from collect import collect

def test_owners():
    for triggers in collect().values():
        for trigger in triggers:
            assert trigger.owners
