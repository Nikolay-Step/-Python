# task 3
with open('text2.txt', 'r') as file:
    print('оклад менее 20000 рублей имеют:')
    all_salary = []
    aver_salary = 0
    for line in file:
        # count += 1
        my_list = line.split()
        if float(my_list[1]) < 20000:
            print(my_list[0])
        all_salary.append(float(my_list[1]))
    aver_salary = sum(all_salary)/len(all_salary)
    print(aver_salary)
