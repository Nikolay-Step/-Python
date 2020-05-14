# Task 2
var_list = []
v_count = 0
iterat_count = 0
user_string = input('Введите несколько значений через пробел:')

for word in user_string.split():
    var_list.append(word)
pairs_count = len(var_list) // 2

while iterat_count != pairs_count:
    var_list[v_count], var_list[v_count + 1] = var_list[v_count + 1], var_list[v_count]
    v_count += 2
    iterat_count += 1
print(var_list)

