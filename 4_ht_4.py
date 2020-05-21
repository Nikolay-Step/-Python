# task 4
from functools import reduce
from math import fmod
my_list = [el for el in range(100, 1001) if fmod(el, 2) == 0]


def my_func(prev_el, el):
    return prev_el * el


print(my_list)
print(reduce(my_func, my_list))
