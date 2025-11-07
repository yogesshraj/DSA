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

c = [4,5,3,7,3,8,5,7,8]
p = len(c)
for i in range(p-1):
    swapped = False
    for j in range(p-i-1):
        if c[j] > c[j+1]:
            c[j], c[j+1] = c[j+1], c[j]
            swapped = True
    if not swapped:
        break
print(c)

# much more faster by skipping the sorted fields

d = [54,2,56,7,7,33,6,7,4,6,74,34,6,65]
z = len(d)
for i in range(z-1):
    swapped = False
    for j in range(z-i-1):
        if d[j] > d[j+1]:
            d[j], d[j+1] = d[j+1], d[j]
            swapped = True
    if not swapped:
        break

print(d)


e = [5,3,3,6,7,2,7,3,4,7,3,42,4]
for i in range(len(e)):
    swapped = False
    for j in range(len(e)- i - 1):
        if e[j] > e[j+1]:
            e[j], e[j+1] = e[j+1], e[j]
            swapped= True
    if not swapped:
        break
print(e) 

new_arr = [5,6,7,32,5,6,7,3,6,7,3,657]
legnth = len(new_arr)
for i in range(legnth-1):
    swapped = False
    for j in range(legnth-i-1):
        if new_arr[j] < new_arr[j+1]:
            new_arr[j], new_arr[j+1] = new_arr[j+1], new_arr[j]
            swapped = True
    if not swapped:
        break
    
print(new_arr)