# sp = [55, 111, True, "sssss", [55,77,88] ]

# for i in range(len(sp)):
#     print(sp[i], end = " ")

# print(end = "\n")
# for el in sp:
#     print(el, end = " ")

# print(end = "\n")
# for item in enumerate(sp):
#     print(item)


from random import randint
import time

def show_test(upper: int) -> str :
    print(randint(1,upper))
    print(time.time() )
    return 1234


print(show_test(100))