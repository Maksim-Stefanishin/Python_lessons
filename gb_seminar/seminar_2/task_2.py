# Задача №11. Решение в группах
# Дано натуральное число A > 1. Определите, каким по 
# счету числом Фибоначчи оно является, то есть 
# выведите такое число n, что φ(n)=A. Если А не 
# является числом Фибоначчи, выведите число -1.
# Input: 5
# Output: 6

def fibo (a):
    count = 2
    fibonachi = 0
    first = 0
    two = 1
    while fibonachi < a:
        fibonachi = first + two
        first = two
        two = fibonachi
        count+=1

    if fibonachi == a:
        print(count)

    else:
        print("-1")

try:
    a = int(input("Введите число А: "))
    print (fibo(a))
except:
    print("Введите корректные данные")


a = int(input("Введите число А: "))




print (fibo(a))

        