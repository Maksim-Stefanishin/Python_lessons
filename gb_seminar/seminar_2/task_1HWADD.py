# Задача 1 HARD по желанию  
# Напишите программу, которая принимает на вход целое или дробное число  
# и выдаёт количество цифр в числе. 
# 456 -> 3 
# 0 -> 1 
# 89,126 -> 5 
# 0,001->4 
 
from decimal import Decimal 
 
number = Decimal(input('Введите число: ')) 
 
if number < 0: 
    number =abs(number) 
    
 
left = int(number) 
right = number - left 
count = 0 
     
if int(number) == 0: 
    count = 1 
    
 
 
 
while left > 0: 
    count += 1 
    left = left // 10 
 
 
while right % 1 != 0: 
    count += 1 
    right *=10 

print(f"Колличество цифр = {count}")