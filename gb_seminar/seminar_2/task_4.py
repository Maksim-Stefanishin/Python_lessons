# 15. Иван Васильевич пришел на рынок и решил
# купить два арбуза: один для себя, а другой для тещи.
# Понятно, что для себя нужно выбрать арбуз
# потяжелей, а для тещи полегче. Но вот незадача:
# арбузов слишком много и он не знает как же выбрать
# самый легкий и самый тяжелый арбуз? Помогите ему!
# Пользователь вводит одно число N – количество
# арбузов. Вторая строка содержит N чисел,
# записанных на новой строчке каждое. Здесь каждое
# число – это масса соответствующего арбуза
# Input: 5 -> 5 1 6 5 9
# Output: 1 9


import random
def find_max_min_mass(count_watermelon):
    max, min = 1, 21 
    for i in range(count_watermelon):
        mass = random.randrange(1,20)
        print(mass, end = " ")
        if max < mass:
            max = mass
        if min > mass:
            min = mass
    print(end = "\n")
    return min, max

count_watermelon = int(input("Введите кол-во арбузов: "))

print(find_max_min_mass(count_watermelon))