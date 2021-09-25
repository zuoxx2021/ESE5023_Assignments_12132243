import numpy as np

M1 = np.random.randint(51, size=(5, 10))
M2 = np.random.randint(51, size=(10, 5))
result = np.zeros((5, 5))


# print(M1)
# print(M2)


def Matrix_multip(m1, m2):
    for i in range(5):
        for j in range(5):
            for k in range(10):
                result[i, j] += m1[i, k] * m2[k, j]
    print(result)


Matrix_multip(M1, M2)
