# Задача 34: Винни-Пух попросил Вас посмотреть, есть ли в его стихах ритм. Поскольку
# разобраться в его кричалках не настолько просто, насколько легко он их придумывает, Вам
# стоит написать программу. Винни-Пух считает, что ритм есть, если число слогов (т.е. число
# гласных букв) в каждой фразе стихотворения одинаковое. Фраза может состоять из одного
# слова, если во фразе несколько слов, то они разделяются дефисами. Фразы отделяются друг
# от друга пробелами. Стихотворение Винни-Пух вбивает в программу с клавиатуры. В ответе
# напишите “Парам пам-пам”, если с ритмом все в порядке и “Пам парам”, если с ритмом все не
# в порядке
# Ввод:                                     Вывод:
# пара-ра-рам рам-пам-папам па-ра-па-дам    Парам пам-пам

# def count_letters(text, letters):
#     my_set = set()
#     for elem in text:
#         counter = 0
#         for letter in elem:
#             if letter in letters:
#                 counter += 1
#         my_set.add(counter)
#     return len(my_set) == 1

# poem = input('Введите стихи: ').split()
# vowels = ['а', 'у', 'о', 'ы', 'и', 'э', 'я', 'ю', 'ё', 'е']

# if count_letters(poem, vowels):
#     print('Парам пам-пам')
# else:
#     print('Пам парам')


# Второй вариант!!
def count_letters(characteristic, objects):
    return len(set(map(characteristic, objects))) == 1

poem = input('Введите стихи: ').split()

if count_letters(lambda x: sum(1 for i in x if i in "аоуыэеёиюя"), poem):
    print("Парам пам-пам")
else:
    print("Пам парам")