@decorator
def func():
    pass

# is equivalent to

def func():
    pass

func = decorator(func)

##############################

@decorator(arg)
def func():
    pass

# is equivalent to

def func():
    pass

func = decorator(arg)(func)


##############################

@dec1(arg)
@dec2
def func():
    pass

# is equivalent to

def func():
    pass

func = dec1(arg)(dec2(func))
