# task 2
count = 0
with open('text.txt', 'r') as file:
    for line in file:
        count += 1
        print('Строка', count, 'имеет', len(line)-1, 'символа')
