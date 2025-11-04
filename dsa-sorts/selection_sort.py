a = [64, 34, 25, 5, 22, 11, 90, 12]
n = len(a)
for i in range(n-1):
    min_index = i
    for j in range(i+1,n):
        if a[j] < a[min_index]:
            min_index = j
    min_value = a.pop(min_index)
    a.insert(i, min_value)

print(a)


b = [5.4,6,7,4,2,6,7,4,7,7]
o = len(b)
for i in range(o-1):
    min_index = i
    for j in range(i+1, o):
        if b[j] < b[min_index]:
            min_index = j
    min_value = b.pop(min_index)
    b.insert(i, min_value)

print(b)


c = [6,3,3,6,7,4,6,8,282,6,2,4,743,3,36,33]
p = len(c)
for i in range(p-1):
    min_index = i
    for j in range(i+1, p):
        if c[j] < c[min_index]:
            min_index = j
    min_value = c.pop(min_index)
    c.insert(i, min_value)

print (c)

d = [53,57,2,47,42,87,21,46,88,1994,436,363,2857,2827,272,22,592]
q = len(d)
for i in range(q-1):
    min_index = i
    for j in range(i+1, q):
        if d[j] < d[min_index]:
            min_index = j
    min_value = d.pop(min_index)
    d.insert(i, min_value)

print(d)

f = [38,383,38538,24,482,8582,848,282,482,48258,858,82,482]
r = len(f)
for i in range(r-1):
    min_index = i
    for j in range(i+1, r):
        if f[j] <f[min_index]:
            min_index = j
    f[i], f[min_index] = f[min_index], f[i]
print(f)

g = [34,5,3,23,53,24,6,7,66,34,23,23,76,24,523]
s = len(g)
for i in range(s-1):
    min_index = i
    for j in range(i+1, n):
        if g[j] < g[min_index]:
            min_index = j
    g[i], g[min_index] = g[min_index], g[i]

print(g)