
#bubble sort
a = [5,6,2,6,7,7,1,2]

n = len(a)

for i in range(n):
    for j in range(n-i-1):
        if a[j] > a[j+1]:
            a[j], a[j+1] = a[j+1], a[j]

print(a)

#selection sort
a = [5,6,2,6,7,7,1,2]
n = len(a)
for i in range(n):
    min_index = i
    for j in range(i+1, n):
        if a[j] < a[min_index]:
            min_index = j
    min_value = a.pop(min_index)
    a.insert(i, min_value)

print(a)

#selection sort with swapping values(best selection sort)
a = [5,6,2,6,7,7,1,2]
n = len(a)
for i in range(n):
    min_index = i
    for j in range(i+1, n):
        if a[j]< a[min_index]:
            min_index = j
    a[i], a[min_index] = a[min_index], a[i]

print(a)


for i in range(0,-1,-1):
    print(i)