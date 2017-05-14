import functools


def decorator(fn):
    print("Decorating function")
    return fn


@decorator
def func(arg1, arg2):
    pass

##########################################################

def decorator(fn):
    @functools.wraps(fn)  # preserve function's metadata
    def wrapper(*args, **kwargs):
        print("Before the function runs")
        return fn(*args, **kwargs)
        print("After the function runs")

    print("Decorating function")
    return wrapper


@decorator
def func(arg1, arg2):
    pass

##########################################################

def decorator(arg1, arg2):
    def actual_decorator(fn):
        return fn

    print("Decorating function")
    print(arg1, arg2)
    return actual_decorator


@decorator(arg1, arg2)
def func(arg3, arg4):
    pass

##########################################################

def decorator(arg1, arg2):
    def actual_decorator(fn):
        @functools.wraps(fn)  # preserve function's metadata
        def wrapper(*args, **kwargs):
            print("Before the function runs")
            return fn(*args, **kwargs)
            print("After the function runs")
        return wrapper

    print("Decorating function")
    print(arg1, arg2)
    return actual_decorator

@decorator(arg1, arg2)
def func(arg3, arg4):
    pass
