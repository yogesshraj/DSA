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