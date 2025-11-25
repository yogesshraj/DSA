# a = [1, 5, 3, 3, 3, 2, 4]
a = [3,4,5,4,3]
def hashmap(a, target):
    obj = {}
    pairs = 0
    for i in a:
        add_ons = target-i
        pairs += obj.get(add_ons, 0)
        obj[i] = obj.get(i, 0)  +1
    # print(pairs)
    return pairs

print(hashmap(a, 7))

wow = [2, 2, 3, 3, 4, 4]
def find_freq(a, target):
    freq= {}
    total_pairs = 0 
    for i in range(len(a)):
        relevant_pair = target - a[i]
        total_pairs += freq.get(relevant_pair, 0)
        freq[a[i]] = freq.get(a[i], 0) +1
    return total_pairs
print(find_freq(wow, 6))


# def total_pairs (a, t):
#     count = {}
#     pairs = 0
#     for l in range(len(a)):
#         friend = t - a[l]
#         pairs += count.get(friend, 0)
#         count[a[l]] = count.get(a[l], 0) +1
#     print(pairs)
# total_pairs(arrss, target)

arrss = [1, 5, 3, 3, 3, 2, 4]
target = 6
def total_pairs (a,t ):
    hashmap = {}
    pairs = 0
    n = len(a)
    for i in range(n):
        friend = t - a[i]
        pairs += hashmap.get(a[friend], 0)
        hashmap[a[i]] = hashmap.get(a[i], 0)+1
    print(pairs)
total_pairs(arrss, target)

arrss = [1, 5, 3, 3, 3, 2, 4]
target = 6
def hasmap_yo(a, t):
    hashmap_obj = {}
    pairs = 0
    for i in range(len(a)):
        friend_existence =  t- a[i] 
        pairs += hashmap_obj.get(friend_existence, 0)
        hashmap_obj[a[i]] = hashmap_obj.get(a[i], 0) +1
    return pairs
print(hasmap_yo(arrss, target))