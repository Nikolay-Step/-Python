# task_1
def result():
    first_num = float(input('Пожалуйста, введите число, которое хотите раделить:'))
    second_num = float(input('Пожалуйста, введите число, на которое хотите раделить:'))
    try:
        first_num / second_num
    except ZeroDivisionError:
        second_num = float(input('Пожайлуста, введите число не равное нулю:'))
    func_result = first_num / second_num
    return func_result


# print_result = result()
print(round(result(), 2))
