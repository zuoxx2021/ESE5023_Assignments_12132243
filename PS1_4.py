def Least_moves(x):
    i = 1
    while x >= 2 ** (i + 1):
        i += 1
    j = x - 2 ** i
    n = i + j
    print(n)


Least_moves(32)
