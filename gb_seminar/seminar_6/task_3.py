# Задача №41. Решение в группах
# Дан массив, состоящий из целых чисел. Напишите
# программу, которая в данном массиве определит
# количество элементов, у которых два соседних и, при
# этом, оба соседних элемента меньше данного. Сначала
# вводится число N — количество элементов в массиве
# Далее записаны N чисел — элементы массива. Массив
# состоит из целых чисел. (круговые массивы)

# Ввод:           Ввод:
# 5               5
# 1 2 3 4         5 1 5 1 5 1
# Вывод:          Вывод:
# 1               3
import random


#n = int(input("Введите размер массива: "))
#array = [random.randint(0,5) for _ in range(n)]
array = [1, 2, 3, 4]
count = 0
#array_res = [x for x in range(n) if array[x] < ]
for i in range(-1, len(array)-1):
    if array[i] > array[i-1] and array[i] > array[i+1]:
        count += 1

print(array)
print(count)


list_1 = [9,8,15,5, 2, 1, 10]

# count = 0
# for i in range(-1, len(list_1)-1):
#     if list_1[i] > list_1[i+1] and list_1[i] > list_1[i-1]:
#         count +=1
#         print(list_1[i])
# print(count)

# print(sum([1 for x in range(-1, len(list_1)-1) if list_1[x] > list_1[x+1] and list_1[x] > list_1[x-1]]))
print(sum([1 for x in range(-1, len(list_1)-1) if list_1[x-1] < list_1[x] > list_1[x+1]]))