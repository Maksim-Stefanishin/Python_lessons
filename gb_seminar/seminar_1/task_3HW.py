#Вы пользуетесь общественным транспортом? Вероятно, вы расплачивались за проезд и получали билет с номером.

#Счастливым билетом называют такой билет с шестизначным номером, где сумма первых трех цифр равна сумме последних трех.

#.е. билет с номером 385916 – счастливый, т.к. 3+8+5=9+1+6.

#Вам требуется написать программу, которая проверяет счастливость билета с номером n и выводит на экран yes или no.
n = int(input("Введите 6-и значный номер : "))

a = n%10 # последняя цифра числа
b = n%100//10
c = n%1000//100
d = n%10000//1000
e = n%100000//10000
f = n%1000000//100000 # первая цифра числа

if (a+b+c) == (d+e+f):
    print("Yes")
else:
    print("No")