# задача 1 сложная необязательная Посчитать сумму цифр любого целого или вещественного числа, число вводит пользователь. Через строку решать нельзя.
import decimal
number = decimal.Decimal(input("Введите число: "))
sum= 0
while number%10  > 0:
    number = number * 10    
while number > 0:
    sum = int(sum + number%10)
    number = number / 10      
print(f"Сумма цифер числа: {sum}")

    
