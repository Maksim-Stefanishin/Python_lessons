# Задача 30:  Заполните массив элементами арифметической прогрессии. Её первый элемент,
# разность и количество элементов нужно ввести с клавиатуры. Формула для получения n-го члена прогрессии: an = a1 + (n-1) * d.
# Каждое число вводится с новой строки.

def fillArray(first_number, pace_number, end_number):  
    arr = []
    for _ in range(end_number):
        n = first_number + _ * pace_number
        arr.append(n)  
    print(arr)


first_number = int(input("Введите начало прогрессии: "))
pace_number = int(input("Введите шаг прогрессии: "))
end_number = int(input("Введите колличество элементов прогрессии: "))

fillArray(first_number, pace_number, end_number)