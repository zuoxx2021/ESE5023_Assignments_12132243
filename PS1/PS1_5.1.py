import random

def Find_expression(a):
    num = '123456789'
    sym = ['+', '-', '']
    for s1 in sym:
        for s2 in sym:
            for s3 in sym:
                for s4 in sym:
                    for s5 in sym:
                        for s6 in sym:
                            for s7 in sym:
                                for s8 in sym:
                                    re = num[-9] + s1 + num[-8] + s2 + num[-7] + s3 + num[-6] + s4 + num[
                                        -5] + s5 + num[-4] + s6 + num[-3] + s7 + num[-2] + s8 + num[-1]
                                    if eval(re) == a:
                                        print(re, ' = ', eval(re))


Find_expression(random.randint(1,100))
Find_expression(1)
