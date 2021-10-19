# Flowchart
import random


def Print_values(a, b, c):
    if a > b:
        if b > c:
            print(a, b, c)
        elif a > c:
            print(a, c, b)
        else:
            print(c, a, b)
    elif b > c:
        pass
    else:
        print(c, b, a)


a = random.randint(0, 100)
b = random.randint(0, 100)
c = random.randint(0, 100)
print("a: ", a)
print("b: ", b)
print("c: ", c)
Print_values(a, b, c)
