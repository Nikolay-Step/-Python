# Task 4
user_string = input('Введите несколько слов через пробел:')
word_count = 1
for word in user_string.split():
    word_for_print = word
    print(str(word_count) + ') ' + word_for_print[0:10])
    word_count = word_count + 1
