# Определите, можно ли от шоколадки размером a × b долек отломить c долек, если разрешается сделать один разлом по прямой между дольками (то есть разломить шоколадку на два прямоугольника).

# Выведите yes или no соответственно.

# Пример:


# a, b, c = 3, 2, 4 -> yes
# a, b, c = 3, 2, 1 -> no

a = int(input("Ведите 1ю сторону прямоугольника: "))
b = int(input("Ведите 2ю сторону прямоугольника: "))
c = int(input("Введите колличество долек: "))
if a*b < c:
    print("No")
elif c%a == 0 or c%b == 0:
    print("Yes")
elif c%a != 0: 
    print("No")
elif c%b != 0:
    print("No")
