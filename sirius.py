a = []
b = []
f = 0

for i in range(1, 18, 2):
    a.append(i)
for j in range(len(a)):
    c = 4 / a[j]
    b.append(c)
for k in range(len(b) - 1):
    if k // 2 != 0:
        f -= b[k]
    else:
        f += b[k]
print(a)
print(b)
print(f)