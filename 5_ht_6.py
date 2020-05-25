# task 6
import re
sum_list = 0
file_dict = {}
with open("text.txt") as file:
    for line in file:
        key, *value = line.split()
        file_dict[key] = value
        result_list = (re.findall(r'\d+', line))
        for el in result_list:
            sum_list += int(el)
        print(key, sum_list)
