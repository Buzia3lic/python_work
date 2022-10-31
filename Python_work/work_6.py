# Вводится список целых чисел в одну строчку через пробел. Необходимо оставить
# в нем только двузначные числа. Реализовать программу с использованием функции
# filter. Результат отобразить на экране в виде последовательности оставшихся чисел в одну строчку через пробел.
# lst = list(map(int, input().split()))
# print(*list(filter(lambda x: 9 < x < 100, lst)))


# 2. Дан список, вывести отдельно буквы и цифры.
# a = ( ‘1’, "a", 'b', '2', '3' ,'c')
# b = ( 'a' , 'b' , 'c')
# c = ( '1', '2', '3')
# lst = ['1', 'vb', '2', 'fg']
# print([i for i in lst if i.isdigit()])
# print([i for i in lst if i.isalpha()])


# 3. Преобразовать набор списков (используя функцию zip)
# from itertools import zip_longest
# #
# users = ['user1','user2','user3','user4','user5']
# ids = [4, 5, 9, 14, 7]
# salary = [111,222,333]
# в другой набор
# ['user1', 4, 111]
# ['user2', 5, 222]
# ['user3', 9, 333]
# и потом вернуть в исходное состояние
# ['user1', 'user2', 'user3']
# [4, 5, 9]
# [111, 222, 333]
# temp = [list(i) for i in zip_longest(users, ids, salary, fillvalue='')]
# for i in range(len(temp)):
#     temp[i] = list(filter(lambda x: x, temp[i]))
# print(temp)
# print(list(zip_longest(*temp)))

# Напишите программу для обработки текста.
# На вход вашей программы подаётся многострочный текст, причём число строк заранее неизвестно.
# Ваша задача – пронумеровать слова в нём, начиная с нуля, а затем вывести только те слова, которые начинаются с большой буквы.
# Перед словом необходимо вывести номер первого вхождения этого слова в текст.
# text = []
# dic = {}
# for i in range(4):
#     text.extend(input().replace('.', '').split())
# for i, k in enumerate(text):
#     if k[0].isupper():
#         if k not in dic:
#             dic[k] = i
# for k, v in sorted(dic.items()):
#     print(f'{v} - {k}')

