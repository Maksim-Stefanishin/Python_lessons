# Задача НЕГАФИБОНАЧЧИ по желанию 
# Задайте число. 
# Составьте список чисел Фибоначчи,  
# в том числе для отрицательных индексов. 
 
# Пример: 
 
# для k = 8 список будет выглядеть так:  
# [-21 ,13, -8, 5, −3, 2, −1, 1, 0, 1, 1, 2, 3, 5, 8, 13, 21] [Негафибоначчи] 

def Fibonacci_array(n, fib1, fib2):
    fibo_array =[fib1, fib2]
    for _ in range(2, n):
        fib1, fib2 = fib2, fib1 + fib2
        fibo_array.append(fib2)
    

    
    
    reversed_array= [0,]
    for _, value in enumerate(fibo_array):
        if _%2 != 0:
            value= -value 
        reversed_array.append(value)
               
    
    reversed_array = list(reversed(reversed_array))
    array =  reversed_array + fibo_array 
    print(array)





fib1 = fib2 = 1
n = int(input('Введите длину последовательности Фибоначчи: '))


Fibbonachi_array(n, fib1, fib2)

