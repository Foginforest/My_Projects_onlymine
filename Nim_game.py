a = 5

x = [[0 for i in range(a)] for j in range(a)]

for i in range(len(x)):
    x[i][a - 1] = 'end'

print(x)