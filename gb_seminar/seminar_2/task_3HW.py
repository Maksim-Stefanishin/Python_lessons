# Задача 14: Требуется вывести все целые степени двойки (т.е. числа вида 2^k), не превосходящие числа N.


def printPowArray (number,counter):
    powArray = []
    while counter <= number:
        powArray.append(counter)          
        counter*=2
    print(powArray)
    

number = int(input("Введите число: "))
counter = 2

printPowArray(number, counter,)

