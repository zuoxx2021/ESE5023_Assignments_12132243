import numpy as np


def Pascal_triangle(k):
    m1 = np.zeros((k, k))
    m1[0, 0] = 1
    m1[1, 0] = 1
    m1[1, 1] = 1

    if k == 1:                                        #第1行
        print(int(m1[0, 0]))
    elif k == 2:                                      #第2行
        print(int(m1[1, 0]), int(m1[1, 1]))
    else:
        for i in range(2, k):                         #第3行及以后,i表示行号
            m1[i, 0] = 1                              #每一行第一个值均为1
            for j in range(1, i + 1):                        
                m1[i, j] = m1[i - 1][j - 1] + m1[i - 1][j]
                #自第二个值开始，元素的值等于上方元素与左上方元素相加
    
    for j in range(k):
        print(int(m1[k-1,j]),end =' ')
    print('\n__________________________________________________________')


Pascal_triangle(100)
Pascal_triangle(200)
