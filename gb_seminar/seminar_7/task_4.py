# Необходимо написать программу для автоматического перевода различных валютных счетов в рублевые.
# Начальные данные программы это три различных списка - Фамилии владельцев банковских счетов, указание валют счетов, 
# соответствующее состояние счетов. То есть у Иголкина счет в евро и там лежит 50000, и так далее.
# Также вначале заданы отношения курса рубля к доллару и евро.

# surnames = ["Иванов", "Карпов", "Иголкин"]
# currency_name = ["рубль", "доллар", "евро"]
# balances = [30000, 40000, 50000]
# dollar = 90
# euro = 99

# Вам необходимо написать функцию calc, которая на входе принимает только один аргумент, далее надо применить ее в комбинациях с map и zip.

# На выходе программы должны быть три пары значений - фамилии владельцев счетов и состояние рублевого счета.

def calc(people_money):
    #res = list(map(lambda x : (x[0],x[2]*dollar) if x[1] == "доллар" else (x[0], x[2]) , people_money))
    res = people_money[1]
    if people_money[0] == "доллар":
        res *= dollar
    elif people_money[0] == "евро":
        res *= euro
    return res


surnames = ["Иванов", "Карпов", "Иголкин"]
currency_name = ["рубль", "доллар", "евро"]
balances = [30000, 40000, 50000]
dollar = 90
euro = 99

#people_money = list(zip(currency_name, balances))
new_balances = list(map(calc,zip(currency_name, balances)))
#print(people_money)
#print(calc(people_money))
print(*zip(surnames, new_balances))