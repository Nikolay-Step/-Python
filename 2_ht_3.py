# Task3
month_list = ['Январь', 'Февраль', 'Март', 'Апрель', 'Май', 'Июнь',
              'Июль', 'Август', 'Сеньтябрь', 'Октябрь', 'Ноябрь', 'Декабрь']
user_input = int(input('Пожалуйста введите номер месяца от 0 до 11, начиная с Января: '))
# # List
print('Решение через List')
if 0 <= user_input <= 1 or user_input == 11:
    print('Вы выбрали месяц ' + month_list[user_input]+ '. Это зима')
elif 2 <= user_input <=4:
    print('Вы выбрали месяц ' + month_list[user_input] + '. Это Весна')
elif 5 <= user_input <=7:
    print('Вы выбрали месяц ' + month_list[user_input] + '. Это Лето')
else:
    print('Вы выбрали месяц ' + month_list[user_input] + '. Это Осень')

# # Dict
print('Решение через Dict')

month_dict = {11: 'Декабрь', 0: 'Январь', 1: 'Февраль', 2: 'Март',
              3: 'Апрель', 4: 'Май', 5: 'Июнь', 6: 'Июль', 7: 'Август',
              8: 'Сентябрь', 9: 'Октябрь', 10: 'Ноябрь'}

print(month_dict.get(user_input))
if 0 <= user_input <= 1 or user_input == 11:
     print('Вы выбрали месяц ' + month_dict.get(user_input) + '. Это зима')
elif 2 <= user_input <=4:
     print('Вы выбрали месяц ' + month_dict.get(user_input)+ '. Это Весна')
elif 5 <= user_input <=7:
     print('Вы выбрали месяц ' + month_dict.get(user_input) + '. Это Лето')
else:
     print('Вы выбрали месяц ' + month_dict.get(user_input) + '. Это Осень')
