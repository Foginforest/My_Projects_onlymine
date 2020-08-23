a = 'aaabbbcbbaab'
b = []
c = []
count = 1
for i in range(len(a) - 1):
    b.append(a[i])
    if a[i + 1] not in b or i + 1 == len(a) - 1:
        n = b.count(a[i])
        c.append(set(b))
        c.append(n)
        b = []
print(c)
