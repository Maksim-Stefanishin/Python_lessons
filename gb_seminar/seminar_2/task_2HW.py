# Задача 12: Петя и Катя – брат и сестра. Петя – студент, а Катя – школьница.
# Петя помогает Кате по математике. Он задумывает два натуральных числа X и Y (X,Y≤1000), а Катя должна их отгадать.
#  Для этого Петя делает две подсказки. Он называет сумму этих чисел S и их произведение P.
#                                                                                                                                                           Помогите Кате отгадать задуманные Петей числа.




def guess_number(sum, product, numbers):
    num1 = 0
    num2 = 0
    for num1 in numbers:
        for num2 in numbers:
         if num1 + num2 == sum and num1 * num2 == product and num1 > 0 and num2 > 0:
            num1, num2 = num1, num2
            print(f"Загаданные числа {num1}, {num2}")             
            return(num1, num2)
                



sum = int(input("Введите сумму двух чисел: ")) 
product = int(input("Введите произведение двух чисел: ")) 
numbers = sorted(set(range(1, 1001))) 

guess_number(sum, product, numbers)

