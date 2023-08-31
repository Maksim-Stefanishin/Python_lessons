# Хакер Василий получил доступ к классному журналу и
# хочет заменить все свои минимальные оценки на
# максимальные. Напишите программу, которая
# заменяет оценки Василия, но наоборот: все
# максимальные – на минимальные.
# Input: 5 -> 1 3 3 3 4
# Output: 1 3 3 3 1

def Change_Array(array, max_array, min_array):
    for i in range(len(array)):
        if array[i] == max_array:
            array[i] = min_array
    return array






array = [1, 3, 3, 3, 4]
max_array = max(array)
min_array = min(array)
print(Change_Array(array, max_array, min_array))