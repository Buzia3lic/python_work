# 1. Дан список. Выведите те его элементы, которые встречаются в списке только один раз. 
# Элементы нужно выводить в том порядке, в котором они встречаются в списке.
# Входные данные	Выходные данные
# 1 2 2 3 3 3	1

# #list = []
# list = [int(i) for i in input('Введите числа через пробел: ').split()]
# list2 = []
# # num = int(input('Введите количество: '))
# # for i in range(num):
# #     list.append(int(input(f'Введите число {i + 1}: ')))

# for i in range(len(list)):
#     for j in range(i + 1, len(list)):
#         if list[i] == list[j]:
#             list2.append(list[i])
#             list2.append(list[j])
# for el in list2:
#     list.remove(el)
# print(list)


# 2. Дан список чисел. Выведите все элементы списка, которые больше предыдущего элемента.
# Входные данные	Выходные данные
# 1 5 2 4 3	5 4

# list = []
# list2 = []
# num = int(input('Введите количество: '))
# for i in range(num):
#     list.append(int(input(f'Введите число {i + 1}: ')))

# print(len(list))

# for i in range(1, len(list)):
#     if list[i] > list[i - 1]:
#         list2.append(list[i])
# print(list2)

# 3. Реализуйте алгоритм задания случайных чисел 
# без использования встроенного генератора псевдослучайных чисел.

# from datetime import datetime
# num = int(input('Введите длину: '))
# print(datetime.now().microsecond % 10**num)

# 4. Задайте список. Напишите программу, которая определит, 
# присутствует ли в заданном списке строк некое число.

# num = input('Введите строку: ')
# check = False
# for el in num:
#     if el.isdigit():
#         check = True
#         break
# if check == True:
#     print('Yes')
# else:
#     print('No')

# 5. Напишите программу, которая определит позицию второго 
# вхождения строки в списке либо сообщит, что её нет.
# список: ["qwe", "asd", "zxc", "qwe", "ertqwe"], ищем: "qwe", ответ: 3
# список: ["йцу", "фыв", "ячс", "цук", "йцукен", "йцу"], ищем: "йцу", ответ: 5

# list = ["qwe", "asd", "qwe", "zxc", "qwe", "ertqwe"]
# print(list)
# find = input('Введите строку для поиска: ')
# count = 0

# for i in range(len(list)):
#     if list[i] == find:
#         count += 1
#         if count == 2:
#             print(i)




