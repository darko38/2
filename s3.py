# 1. Задайте список. Напишите программу, которая определит, присутствует ли в заданном списке строк некое число.

# my_list = ['dfgr23kdkld', 'oijkn23e2', 'fjkdfjvn', '2342ewefcdsf432']
# number = input('Введите символ : ')

# for item in my_list:
#     print(item)
#
# print('\n')
#
# for i in range(len(my_list)):
#     print(my_list[i])

# n = 0
# for item in my_list:
#     for symbol in item:
#         if symbol == number:
#             print(f'Символ {number} присутствует в строке {item}')
#             break
#     else:
#         print(f'Символ {number} НЕ присутствует в строке {item}')
# for item in my_list:
#     if number in item:
#         print(f'Символ {number} присутствует в строке {item}')
#     else:
#         print(f'Символ {number} НЕ присутствует в строке {item}')

# for item in my_list:
#     for symbol in item:
#         if symbol == number:
#             n+=1
#             print(f'Символ {number} присутствует в строке {item} {n} раз(а)')
#             break
#     else:
#         print(f'Символ {number} НЕ присутствует в строке {item}')

# for item in my_list:
#     n = 0
#     for i in range(len(item)):
#         if number == item[i]:
#             n += 1
#             print(f'Символ {number} присутствует в строке {item}'
#                    f'на {i} позиции')
#     print(f'Символ {number} присутствует в строке {item} {n} раз(а)')

# Разделение строки на отдельные элементы в список и соединение их через join в строку
string = 'asdfgh'
new_string = []
for i in string:
    new_string.append(i)
print(new_string)
# ИЛИ
# print(string)
# string = list(string)
# print(string)
# string = ''.join(string)
# print(string)
# new_string = []
# for i in range(0,len(string), 2):
#     new_string.append(string[i] + string[i+1])
# print(new_string)

# 2. Напишите программу, которая определит позицию второго вхождения строки в списке либо сообщит, что её нет.
#
# *Пример:*
#
# - список: ["qwe", "asd", "zxc", "qwe", "ertqwe"], ищем: "qwe", ответ: 3
# - список: ["йцу", "фыв", "ячс", "цук", "йцукен", "йцу"], ищем: "йцу", ответ: 5
# - список: ["йцу", "фыв", "ячс", "цук", "йцукен"], ищем: "йцу", ответ: False
# - список: ["123", "234", 123, "567"], ищем: "123", ответ: False
# - список: [], ищем: "123", ответ: False

# my_list = ["123", "234", 123, "567"]
# find = '124'
# n = 0
# for i in range(len(my_list)):
#     if find == my_list[i]:
#         n+=1
#     if n==2:
#         print(f'Искомое выражение находится на {i} позиции')
#         break
# else:
#         if n==1:
#             print(f'Искомое выражение не повторяется')
#         else:
#             print(f'Искомое значение не найдено')

# one = 1
# two = 2
#
# string = f'Первое число - {one}, второе число - {two}, третье число - {one + two}'
# print(string)
# string_2 = 'Первое число - ' + str(one) + ', второе число - ' + str(two) + ', третье число - ' + str(one + two)
# print(string_2)
# string_3 = 'Первое число - {}, второе число - {}, третье число - {}'.format(one,two,(one+two))
# print(string_3)

# text = 'Первое число - 1, второе число - 2, сумма 3 чи'
# sub_text = input('Введите подстроку: ')
# count = 0
# for i in range(len(text)):
#     if text[i:i+len(sub_text)] == sub_text:
#         count += 1
# print(f'Подстрока {sub_text} встречается в заданном тексте {count} раз(а)')
# print(text.count(sub_text))


