# Задача №35. Решение в группах
# Напишите функцию, которая принимает одно число и
# проверяет, является ли оно простым
# Напоминание: Простое число - это число, которое
# имеет 2 делителя: 1 и n(само число)
# Input: 5
# Output: yes

# 6 - 1 2 3 6
# 5 - 1 5

# def Find_natural(num, dell):
#     count = 0
#     if dell >= 1 and num % dell == 0:
#         count += 1
#         return Find_natural(num, dell - 1)
#     if dell == 0 and count > 2:
#         return "No"
#     elif dell == 0 and count == 2:
#         return "Yes"

# number = int(input("Введите число: "))
# dell = number
# print(Find_natural(number, dell))   не доделано


# Задача №35. Решение в группах
# Напишите функцию, которая принимает одно число и
# проверяет, является ли оно простым
# Напоминание: Простое число - это число, которое
# имеет 2 делителя: 1 и n(само число)
# Input: 5
# Output: yes

def check_num(n, i):

    if i > n - 1:
        return "yes"
    elif n % i == 0:
        return 'no'
    
    return check_num(n, i + 1)
    

    
        


# num = int(input("Input num: "))
num = 1

print(check_num(num, 2))