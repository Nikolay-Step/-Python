# task_3
def my_func(first_num, sec_num, third_num):
    # first_num = float(input('Введите первое число:'))
    # sec_num = float(input('Введите второе число:'))
    # third_num = float(input('Введите третье число:'))
    if not first_num > sec_num:
        if not first_num > third_num:
            return sec_num + third_num
    elif not sec_num > first_num:
        if not sec_num > third_num:
            return first_num + third_num
    else:
        return first_num + sec_num


print(my_func(first_num=float(input('Введите первое число:')),
              sec_num=float(input('Введите второе число:')),
              third_num=float(input('Введите третье число:'))))
