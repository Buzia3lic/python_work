# list = [int(i) for i in input('Введите числа через пробел: ').split()]
# print(list)

# a = max(list)
# b = min(list)
# print(a, b)


dict = \
    {
        'Hi':'Hello',
        'Bye':'Goodbye',
        'List':'Array'
    }
print(dict)

find = 'Goodbye'

if find in dict.keys():
    print(dict[find])

if find in dict.values():
    ind = list(dict.values()).index(find)
    print(list(dict.keys())[ind])

