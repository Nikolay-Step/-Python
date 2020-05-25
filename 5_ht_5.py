# task 5
file_list = []
result = 0
with open('text.txt', 'w') as file:
    file.write('12 34234 23423234 121 12313')
with open('text.txt', 'r') as file:
    for line in file:
        file_list = line.split()
for el in file_list:
    result += float(el)
print(result)

