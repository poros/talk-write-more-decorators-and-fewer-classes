from functools import partial

# convert base 2 string to an int
basetwo = partial(int, base=2)
assert basetwo('10010') == 18
