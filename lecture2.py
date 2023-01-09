# colors = ['red','green', 'blue']
# data = open('file.txt', 'a')
# # data.writelines(colors) # разделителей не будет
# data.write('LINE 22\n')
# data.write('LINE 33\n')
# data.close()

# with open('file.txt', 'a') as data:
#     data.write('line4\n')
#     data.write('line5\n')

# path = 'file.txt'
# data = open(path, 'r')
# for line in data:
#     print(line)
# data.close
# exit()

# import lecture1.py as l1
# print(l1.f(1))

# def new_string(symbol, count = 3):
#     return symbol * count
# print(new_string('!', 5))
# print(new_string('!'))
# print(new_string(4))

# def concatenatio(*params):
#     res : str = ''  # для работы со строками
#     # res : int = 0 # работы с натуральными числами
#     for item in params:
#         res += item # res = res + item
#     return res
# print(concatenatio('a', '1'))
# print(concatenatio('a', 's', 'd', 'w'))

# РЕКУРСИЯ (???)
def fib(n):
    if n in [1, 2]:
        return 1
    else:
        return fib(n-1) + fib(n-2)
list = []
for e in range (1, 10):
    list.append(fib(e))
print(list)

# a = (3, 1, 41, 4)
# print(a)

# КОРТЕЖИ - неизменяемые списки

# t = ()
# print(type(t))
# t = (1, )
# print(type(t))
# t = (1)
# print(type(t))
# t = (90, 9, 1990)
# print(type(t))
# colors = ['red', 'green', 'blue']
# print(colors)
# print(type(colors))
# colors = tuple(['red', 'green', 'blue'])
# print(colors)
# print(type(colors))
# print(colors[0])
# print(colors[2])
# print(colors[10])
# print(colors[-2])
#
# for e in colors:
#     print(e)

# Создание кортежа из списка
# t = tuple(['red', 'green', 'blue'])
# # red, green, blue = t # Для чего эта строка?
# print('r: {}, g: {}, b: {}'.format('red', 'green', 'blue'))

# СЛОВАРИ
# dictionary = {}
# dictionary = \
#     {
#         'up':'↑',
#         'left':'←',
#         'down': '↓',
#         'right': '→',
#     }
# print(dictionary)
#
# # Чтобы получить ключи (пояснения):
# for k in dictionary.keys():
#     print(k)
#
# #  Чтобы получить значения:
# for v in dictionary.values():
#     print(v)
# for v in dictionary:
#     print(dictionary[v])
#
# dictionary['left'] = '⇦'
# print(dictionary['left'])
# print(dictionary)
#
# del dictionary['left']
# print(dictionary)
#
# for item in dictionary:
#     print('{}: {}'.format(item, dictionary[item]))

# print('{}: {}'.format(item, dictionary[item]))

#  МНОЖЕСТВА
# colors = {'red', 'green', 'blue'}
# print(type(colors))
# print(colors)
#
# colors.add('red')
# print(colors)
#
# colors.add('gray')
# print(colors)
#
# colors.remove('red')
# print(colors)
#
# # colors.remove('red')
# # print(colors)  # при удалении не существующего элемента система выдаст ошибку
#
# colors.discard('red') # через функцию discard система не выдаст ошибку при попытке удаления несуществующего элемента
# print(colors)
#
# colors.clear() # функция clear очищает значения в множестве, оставляя его пустым
# print(colors)

# a = {1, 2, 3, 5, 8}
# b = {2, 5, 8, 13, 21}
# c = a.copy()
# print(c)
# u = a.union(b)
# print(u)
# i = a.intersection(b)
# print(i)
# dl = a.difference(b) # что есть в множестве a, чего нет в b
# print(dl)
# dr = b.difference(a) # что есть в множестве b, чего нет в a
# print(f'dr:{dr}')
#
# s = frozenset(a)
# print(s)

# list1 = [1,2,3,4,5]
# list2 = list1
# for i in list1:
#     print(i)
# print()
# for i in list2:
#     print(i)
#
# При внесении изменений в какой-либо из списков, через '=' будет меняться и второй список
#
# list1[0] = 123
# for i in list1:
#     print(i)
# print()
# for i in list2:
#     print(i)
#
# list2[1] = 333
# for i in list1:
#     print(i)
# print()
# for i in list2:
#     print(i)

# print(list1)
# print(list1.pop()) # функция pop по умолчанию извлекает крайнее слева значение, но в скобках можно указать индекс значения, который нужно извлечь
# print(list1)
#
# print(list1)
# print(list1.pop(2)) # в скобках указан индекс значения, которое нужно ИЗВЛЕЧЬ(!!!)
# print(list1)
#
# list1.insert(2,11) # функция insert вставляет определенное значение на место индекса, сначала в аргументе ставится индекс, а затем сам элемент для вставки
# print(list1)
#
# list1.append(17) # через функцию append происходит добавление элемента на крайнюю справа позицию
# print(list1)

