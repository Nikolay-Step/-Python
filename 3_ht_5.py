# task_5
def my_func(user_input):
    x = 0
    my_list = user_input.split()
    for el in my_list:
        x += int(el)
    return x
print(my_func(user_input=input('введите несколько чисел через пробел')))

