# task 4
o_list = []
n_list = []
with open('old.txt', 'r') as o_file:
    for line in o_file:
        o_list = line.split()
        n_list = o_list
        if o_list[0] == 'One':
            n_list[0] = 'Один'
            with open('new.txt', 'w') as n_file:
                n_file.write(n_list[0] + ' - ' + n_list[2] + '\n')
        elif o_list[0] == 'Two':
            n_list[0] = 'Два'
            with open('new.txt', 'a') as n_file:
                n_file.write(n_list[0] + ' - ' + n_list[2] + '\n')
        elif o_list[0] == 'Three':
            n_list[0] = 'Три'
            with open('new.txt', 'a') as n_file:
                n_file.write(n_list[0] + ' - ' + n_list[2] + '\n')
        elif o_list[0] == 'Four':
            n_list[0] = 'Четыре'
            with open('new.txt', 'a') as n_file:
                n_file.write(n_list[0] + ' - ' + n_list[2] + '\n')
