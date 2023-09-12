# Задача 32: Определить индексы элементов массива (списка), значения которых принадлежат заданному диапазону 
# (т.е. не меньше заданного минимума и не больше заданного максимума). Список можно задавать рандомно

# На входе : [ 1, 5, 88, 100, 2, -4]
# 33
# 200
# Ответ: [2, 3]


from random import randint

def find_indices(min, max, arr):
    indices = []
    for index, value in enumerate(arr):
        if min <= value <= max:
            indices.append(index)
    return indices

arr_size = int(input('Введите размер массива: '))
min = int(input('Введите минимальное значение диапазона: '))
max = int(input('Введите максимальное значение диапазона: '))
arr = [randint(-100, 100) for _ in range(arr_size)]
print(arr)
print(find_indices(min, max, arr))