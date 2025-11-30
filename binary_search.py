import math

def minEatingSpeed(piles, H):
    low = 1
    high = max(piles)
    while low < high:
        mid = math.ceil((low + high)// 2)
        hours = 0
        for p in piles:
            hours += math.ceil(p/mid)
        if hours > H:
            low = mid + 1
        else:
            high = mid
    return low

piles = [3, 6, 7, 11]
H = 8
print(minEatingSpeed(piles, H))   # Output: 4

#Given an array of integers and an integer k, 
# return the length of the longest subarray whose sum equals exactly k.

a = [1, -1, 5, -2, 3]
k = 3
a = [-2, -1, 2, 1] 
k = 1
def how_many_sub_arr(a, k):
    prefix = [0]
    existence = {0:1}
    total_sub_arr = 0
    max_value = 0
    for i in range(len(a)):
        pre_sum = prefix[len(prefix)-1]+ a[i]
        needed_value = pre_sum - k
        if needed_value in existence:
            max_value = max(max_value, i-(prefix.index(needed_value)-1))
            total_sub_arr += existence[needed_value]
        existence[pre_sum] = existence.get(pre_sum, 0) + 1
        prefix.append(pre_sum)

    return max_value
print(how_many_sub_arr(a, k))