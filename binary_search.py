import math as math
piles = [3, 6, 7, 11]
H = 8 
k_min = 1
k_max = max(piles)
k_mid = math.ceil((k_min + k_max) // 2)
total_h = 0
print(k_mid)
for i in piles:
    the_math = math.ceil(i/k_mid)
    total_h += the_math
    print(the_math)
    
print(total_h)