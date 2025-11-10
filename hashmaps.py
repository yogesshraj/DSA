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

hashmap(a, 7)

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
