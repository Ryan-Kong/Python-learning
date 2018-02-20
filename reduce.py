from functools import reduce
def add(x, y):
    return x + y
reduce(add, [1, 3, 5, 7, 9])