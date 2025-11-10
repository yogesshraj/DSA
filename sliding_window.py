k=3
arr = [2, 1, 5, 1, 3, 2]

def max_sum_k(arr, k):
    current_sum = sum(arr[:k])
    max_sum = current_sum
    for i in range(k,len(arr)):
        current_sum =current_sum- arr[i-k] + arr[i]
        if current_sum > max_sum:
            max_sum = current_sum
    return max_sum
print(max_sum_k(arr,k))

#level 2
a = "abcabcbb"

def longest_unique_substring(a):
    left = 0
    best = 0
    hashmap = {}
    for right in range(len(a)):
        hashmap[a[right]] = hashmap.get(a[right], 0) + 1
        while hashmap.get(a[right]) > 1:
            hashmap[a[left]] = hashmap.get(a[left],0) - 1
            left += 1
        best = max(best, right-left+1)
    return best
print(longest_unique_substring(a))

#reverse condition
#Longest substring where every character appears at least once.
#Find the shortest substring that contains all distinct characters of the string.
# s = "aabcbcdbca"
# def distinct_char (s):
#     left = 0
#     best = 0
#     hashmap = {}
#     have = 0
#     for right in range(len(s)):
#         hashmap[s[right]] = hashmap.get(s[right], 0) + 1
#         if hashmap[s[right]] == 1:
#             have += 1
#         if have == len(s):
#             best+=1
#             hashmap[s[left]] = hashmap.get(s[left], 0) - 1
#         while have < len(s):
#             left+=1
#     return best

# print(distinct_char(s))

string = "eceba"
def k_distinct(s, k):
    freq = {}
    best = 0
    left = 0
    for i in range(len(s)):
        freq[s[i]] = freq.get(s[i], 0) +1
        while len(freq) > k:
            freq[s[left]]-=1
            if freq[s[left]] == 0:
                del freq[s[left]]
            left+=1
        best = max(best, i - left + 1)
    print(best)
k_distinct(string, 2)

