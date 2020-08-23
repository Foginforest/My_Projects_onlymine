a = ['a', 'b', 'c', 'd', 'e', 'g']
print(a)
b = [1, 2, 3]

for i in range(len(b)):
    a.remove(a[b[i]])
print(a)