import random


def Least_moves(x):
    i = 1             #i表示操作的次数
    while x != 2:
        if x % 2 != 0:
            x -= 1
            i += 1
        else:
            x /= 2
            i += 1
    print(i)


b = random.randint(2, 100)
print(b)
Least_moves(b)
