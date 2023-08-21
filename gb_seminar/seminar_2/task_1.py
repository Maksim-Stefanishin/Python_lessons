# По данному целому неотрицательному n вычислите
# значение n!. N! = 1 * 2 * 3 * … * N (произведение всех
# чисел от 1 до N) 0! = 1 Решить задачу используя цикл
# while
n = int(input("Введите число N: "))
# while i <= n:
#     factorial*=i
#     i+=1
def factorial(n):
    factorial_n = 1
    i = 1
    while i <= n:
        factorial_n*=i
        i+=1
    print(factorial_n)


factorial(n)