a = [1, 2, 4, 7, 11, 15]
# def pair_sum(a, target):
#     for i in range(len(a)-1):
#         for j in range(len(a)-1,0, -1):
#             if i == j:
#                 break            
#             if a[i] +a[j] == target:
#                 print(i,j)
#                 break

def pair_sum(a, target):
    l, r = 0, len(a)-1
    while l < r:
        s = a[l]+a[r]
        if s == target:
            return (l,r)
        elif s < target:
            l+=1
        else: 
            r-=1
print(pair_sum(a, 15))

b = [1, 3, 4, 5, 7, 10, 11]
def pair_sum_2(b, target):
    l,r = 0, len(b)-1
    while l < r:
        s = b[l]+b[r]
        if s == target:
            return (l,r)
        elif s < target:
            l +=1
        else:
            r-=1
    return None
print(pair_sum_2(b, 17))
print(pair_sum_2([2, 3, 5, 8, 9, 14], 17))
print(pair_sum_2([1, 2, 3, 4], 100))