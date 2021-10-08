import numpy as np

Total_solutions = np.zeros((101, 2))


def Find_expression(a):
    num = '123456789'
    sym = {'+', '-', ''}
    i = 0

    for s1 in sym:
        for s2 in sym:
            for s3 in sym:
                for s4 in sym:
                    for s5 in sym:
                        for s6 in sym:
                            for s7 in sym:
                                for s8 in sym:
                                    re = num[-9] + s1 + num[-8] + s2 + num[-7] + s3 + num[-6] + s4 + num[-5] + s5 + num[
                                        -4] + s6 + num[-3] + s7 + num[-2] + s8 + num[-1]
                                    if eval(re) == a:
                                        i += 1
                                        # print(re, ' = ', eval(re))
    Total_solutions[a][0] = int(a)
    Total_solutions[a][1] = int(i)


for j in range(1, 101):
    Find_expression(j)

print(Total_solutions)
