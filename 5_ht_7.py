# task 7
firm_dict = {}
firm_count = 0
aver_effort = 0
with open("text.txt") as file:
    for line in file:
        key, *value = line.split()
        firm_dict[key] = value
        f_value = 0
        effort_value = 0
        turn_over = 0
        i = 1
        for value in value:
            if i == 2:
                effort_value = int(value)
                i += 1
            elif i == 3:
                turn_over = int(value)
            else:
                i += 1
            f_value = effort_value - turn_over
        if f_value > 0:
            firm_count += 1
            aver_effort += f_value
        print(key, f_value)
    print(aver_effort/firm_count)

# print(firm_dict)



        #   zxc = sum([value for key, value in firm_dict.items()])
            # f_value = int(value[0]) + int(value[1])
    # f_value = value(1) + value(2)
    # print(firm_dict)
