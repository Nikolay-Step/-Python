# task 5
from itertools import count
from itertools import cycle
for el in count(14):
    if el > 78:
        break
    else:
        print(el)

i = 0
my_list = [2, 2, 2, 7, 23, 1, 44, 44, 3, 2, 10, 7, 4, 11]
for el in cycle(my_list):
    if i > 78:
        break
    print(el)
    i += 1

