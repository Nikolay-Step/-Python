# task 2
from functools import reduce
from math import fmod
my_list = [300, 2, 12, 44, 1, 1, 4, 10, 7, 1, 78, 123, 55]


def my_func(prev_el, el):
    if el > prev_el:
        return el
    else:
        return prev_el


new_list = [el for el in my_list if el > reduce(my_func, my_list)]

print(new_list)
