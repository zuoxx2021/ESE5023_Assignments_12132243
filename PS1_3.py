import numpy as np


def Pascal_triangle(k):
    m1 = np.zeros((k, k))
    m1[0, 0] = 1
    m1[1, 0] = 1
    m1[1, 1] = 1

    if k == 1:
        print(int(m1[0, 0]))
    elif k == 2:
        print(int(m1[1, 0]), int(m1[1, 1]))
    else:
        for i in range(2, k):
            m1[i, 0] = 1
            if i == k-1:
                print('\n', int(m1[i, 0]), end=' ')
            for j in range(1, i + 1):
                m1[i, j] = m1[i - 1][j - 1] + m1[i - 1][j]
                if i == k-1:
                    print(int(m1[i, j]), end=' ')


Pascal_triangle(100)
