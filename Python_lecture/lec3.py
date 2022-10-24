# def f(x):
#     return x**2

# g = f

# print(f(1))
# print(g(1))

# def calc(x):
#     return x + 10

# print(calc(10))

# def math(op, x):
#     print(op(x))

# math(calc, 10)

################

# # def sum(x, y):
# #     return x+y

# # sum = lambda x, y: x+y+1

# def mult(x, y):
#     return x*y

# def calc (op, a, b):
#     print(op(a, b))

# #calc(sum, 4, 5)
# calc(lambda x, y: x+y+1, 4 ,5)

############################


# # list = []

# # for i in range(1, 101):
# #     if (i%2 == 0):
# #         list.append(i)

# # print(list)

# def f(x):
#     return x**3

# list = [(i, f(i)) for i in range(1, 21) if i % 2 == 0]
# print(list)

#############################

# def f(x):
#     return x**2

# list1 = [1, 2, 3, 5, 8, 15, 23, 38]

# newlist = [(i, f(i)) for i in list1 if i % 2 == 0]
# print(newlist)

# li = list(map(lambda x: x + 10, list1))

# print(li)
# ########
# data = list(map(int, input().split()))
# print(data)

################


# data = [1, 2, 3, 5, 8, 15, 23, 38]
# res = list(filter(lambda x: not x%2, data))
# print(res)

#################

# users = ['user1', 'user2', 'user3']
# ids = [4, 6, 9]

# data = list(zip(users, ids))
# print(data)


###################3


# users = ['user1', 'user2', 'user3']
# ids = [4, 6, 9]

# data = list(enumerate(users))
# print(data)