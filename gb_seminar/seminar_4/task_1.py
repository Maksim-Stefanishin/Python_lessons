# Напишите программу, которая принимает на вход
# строку, и отслеживает, сколько раз каждый символ
# уже встречался. Количество повторов добавляется к
# символам с помощью постфикса формата _n.
# Input: a a a b c a a d c d d
# Output: a a_1 a_2 b c a_3 a_4 d c_1 d_1 d_2
# Для решения данной задачи используйте функцию
# .split()

# a = "a a a b c a a d c d d"
# dict = {}
# res = ""
# for el in a.split():
#     dict[el] = 0

# for el in a.split():
#     if dict[el] == 0:
#         res = res + el + " "
#     else:
#         res += f"{el}_{dict[el]} "
#     dict[el] = dict[el] + 1
# print(res)

def duplicateQuantity(a):
    dict = {}
    res = ""
    for el in a.split():
        dict[el] = 0

    for el in a.split():
        if dict[el] == 0:
            res = res + el + " "
        else:
            res += f"{el}_{dict[el]} "
        dict[el] = dict[el] + 1
    return res


a = "a a a b c a a d c d d"
print(duplicateQuantity(a))