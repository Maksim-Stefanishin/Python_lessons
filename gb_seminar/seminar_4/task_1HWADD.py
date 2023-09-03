# задача 1 необязательная. 
# Пользователь вводит натуральное k.  
# Надо сформировать многочлен такой степени,  
# где все коэффициенты случайные от -10 до 10. 
 
# например, k=2 -> -x^2 + 3*x - 8 = 0 
# тут коэффициенты -1,3,-8 
# например, k=3 -> 3*x^3 - 2*x = 0 
# тут коэффициенты 3,0,-2,0 
 
from random import randint 
 

 


def polynomial_print(k):
    array = [] 
    polynomial = '' 
    for i in range(k+1): 
        array.append(randint(-10,10))    
    for i, number  in enumerate(array): 
        degree = k -i      
        if degree == 0:         
            if number<0: 
                polynomial += f' - {abs(number)}' 
            else: 
                polynomial += f' + {number}' 
            
        elif degree == 1: 
            if number<0:
                if number == -1: 
                    polynomial += f' - x' 
                else:
                    polynomial += f' - {abs(number)}x'
                
            else:
                if number == 1: 
                    polynomial += f' + x' 
                else:
                    polynomial += f' + {abs(number)}x'
                
        else: 
            if number<0:
                if number == -1: 
                    polynomial += f' - x^{degree}' 
                else:
                    polynomial += f' - {abs(number)}x^{degree}'
                
            else:
                if number == 1: 
                    polynomial += f' + x^{degree}' 
                else:
                    polynomial += f' + {abs(number)}x^{degree}'
    if polynomial[1] == '+':
        polynomial= polynomial[3:]
    else:
        polynomial = polynomial[:2] + polynomial[2+1:]
        polynomial=polynomial.lstrip()
    polynomial+=' = 0'
    print(polynomial)

k = int(input('Введите значение: ')) 
polynomial_print(k)