# Задача 10: На столе лежат n монеток. Некоторые из них лежат вверх решкой, а некоторые – гербом.
# Определите минимальное число монеток, которые нужно перевернуть, чтобы все монетки были повернуты вверх одной и той же
# стороной. Выведите минимальное количество монет, которые нужно перевернуть




from random import randint

def coin_flips(coin_numbers): 
    coins_array = [randint(0,1) for _ in range(coin_numbers)] 
    eagle_count = sum([ coin == 1 for coin in coins_array])
    tails_count = coin_numbers - eagle_count 
    print(coins_array)
    
    if eagle_count > tails_count: 
        print ("Нужно перевернуть ", tails_count , " монет") 
    elif eagle_count == tails_count: 
        print ("Нужно перевернуть ", tails_count  , " монет ") 
    else : 
        print ( "Нужно перевернуть ",  eagle_count,  " монет ") 

coin_numbers  = int ( input ("Введите число монет : ")) 
coin_flips( coin_numbers ) 






    




