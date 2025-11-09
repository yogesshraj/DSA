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
