a = [64, 34, 25, 5, 22, 11, 90, 12]
n = len(a)

for i in range(n-1):
    min_index = i
    for j in range(i+1, n):
        if a[j] < a[min_index]:
            min_index = j
    min_value = a.pop(min_index)
    a.insert(i, min_value)

print(a)

