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
    

    
        


num = int(input("Input num: "))
# num = 1

print(check_num(num, 2))