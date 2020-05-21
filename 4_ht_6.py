# task 6
from math import factorial


def fact():
    res = factorial(5)
    yield res


for el in fact():
    print(el)
