a = [3,7,3,1,8,3,6,3,7,2]
n = len(a)
for i in range(n-1):
    for j in range(n-i-1):
        if a[j] < a[j+1]:
            a[j], a[j+1] = a[j+1], a[j]

# print(a)

aa = [6,7,3,1,5,7,5]
nn = len(aa)
for i in range(nn-3):
    print(i, aa)
    for j in range(nn-i-1):
        if aa[j] < aa[j+1]:
            aa[j], aa[j+1] = aa[j+1], aa[j]
print(aa)

# the above code worked even with nn-3 because it has 2 duplicates(5 and 7) so since we didn't mentioned <=, it passed 
# as it's already sorted.

b = [5,6,3,67,3,7,4,2]
o = len(b)
for i in range(o-1):
    for j in range(o-i-1):
        if b[j] > b[j+1]:
            print(b[j], b[j+1])
            b[j], b[j+1] = b[j+1], b[j]

print(b,"b") 