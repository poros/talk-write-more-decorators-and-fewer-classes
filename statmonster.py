from log import Log  # noqa


def owners(*handlers):
    def decorator(fn):
        fn.owners = handlers
        return fn

    return decorator


def register(*logs):
    def decorator(fn):
        for log in logs:
            log.register(fn)
        return fn

    return decorator
