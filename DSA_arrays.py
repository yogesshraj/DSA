
#bubble sort
a = [5,6,2,6,7,7,1,2]

n = len(a)

for i in range(n):
    for j in range(n-i-1):
        if a[j] > a[j+1]:
            a[j], a[j+1] = a[j+1], a[j]

print(a)