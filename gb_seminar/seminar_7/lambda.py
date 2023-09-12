

x = int(input('Input 1st number: '))
y = int(input('Input 2nd number: '))


def sum(x, y):
    return x + y
f = sum
print(f) # 9

sum = lambda x, y: x + y

print(sum)