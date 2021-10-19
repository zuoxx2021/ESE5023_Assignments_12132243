import matplotlib.pyplot as plt

Total_solutions = []
num = range(1,101)


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
    Total_solutions.append(i)


for j in range(1, 101):
    Find_expression(j)

# plot--------------------------------------------------------------------
# Plot a line
plt.plot(num, Total_solutions)

# Add x and y labels
plt.xlabel("number")
plt.ylabel("Total_solutions")

# find the max and min-----------------------------------------------------
for i in range(100):
    if Total_solutions[i] == max(Total_solutions):
        print('max:',i+1,' Total_solutions:',max(Total_solutions))
    elif Total_solutions[i] == min(Total_solutions):
        print('min:',i+1,' Total_solutions:',min(Total_solutions))