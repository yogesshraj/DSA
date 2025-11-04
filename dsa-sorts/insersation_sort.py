a = [7,3,4,6,7,3,3,6,7,3,2]
b = len(a)
for i in range(1,b):
    insertion_index = i
    current_value = a.pop(i)
    for j in range(i-1, -1,-1):
        if a[j] > current_value:
            insertion_index = j
    a.insert(insertion_index, current_value)

print(a)

c = [3,5,7,3,6,3,5,5,6,3,6,2,3]
d = len(c)
for i in range(1, d):
    insertion_index = i
    index_value = c[i]
    for j in range(i-1, -1, -1):
        if c[j] > index_value:
            c[j+1] = c[j]
            insertion_index = j
        else: 
            break
    c[insertion_index] = index_value
print(c) 