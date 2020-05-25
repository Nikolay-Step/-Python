# task 1
user_input = input('Введие данные или оставьте пустой для выхода:')
text_for_file = []
temp_text_file = ''

while user_input != '':
    temp_text_file += user_input + ' '
    user_input = input('Введие данные или оставьте пустой для выхода:')

list_for_file = temp_text_file.split()
with open("text.txt", 'w') as f:
    for word in list_for_file:
        f.write(word + '\n')




