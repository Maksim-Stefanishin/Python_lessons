# Уставшие от необычно теплой зимы, жители решили узнать,
# действительно ли это самая длинная оттепель за всю историю
# наблюдений за погодой. Они обратились к синоптикам, а те, в
# свою очередь, занялись исследованиями статистики за
# прошлые годы. Их интересует, сколько дней длилась самая
# длинная оттепель. Оттепелью они называют период, в
# который среднесуточная температура ежедневно превышала
# 0 градусов Цельсия. Напишите программу, помогающую
# синоптикам в работе.
# Пользователь вводит число N – общее количество
# рассматриваемых дней (1 ≤ N ≤ 100). В следующих строках
# располагается N целых чисел.
# Каждое число – среднесуточная температура в
# соответствующий день. Температуры – целые числа и лежат в
# диапазоне от –50 до 50
# Input: 6 -> -20 30 -40 50 10 -10
# Output: 2




# from random import randint
# count = 0
# max_count = 0
# number = int(input("Введите число: "))
# i = 1
# temp = []
# while i <= number:
#     temp.append(randint(-50, 50))
#     i+=1
# print(temp)   
# for j in temp:
#     if j > 0:
#         count+=1
#         if count > max_count:
#             max_count = count
#     else:
#         count = 0
# print(max_count)


import random

def count_plus_day(all_count_day):
    count_day = 0
    max_day = count_day
    for i in range(all_count_day):
        grad_day = random.randrange(-50,50)
        print(grad_day, end = " ")
        if grad_day < 1:
            if max_day < count_day:
                max_day = count_day
            count_day = 0
        else:
            count_day += 1
    if max_day < count_day:
        max_day = count_day
    print(end = "\n")
    return max_day


try:
    number = int(input("Введите общее кол-во дней: "))

    print(count_plus_day(number))
except:
    print("Ввели неверные данные")





