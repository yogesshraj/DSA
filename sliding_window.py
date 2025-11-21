# k=3
# arr = [2, 1, 5, 1, 3, 2]

# def max_sum_k(arr, k):
#     current_sum = sum(arr[:k])
#     max_sum = current_sum
#     for i in range(k,len(arr)):
#         current_sum =current_sum- arr[i-k] + arr[i]
#         if current_sum > max_sum:
#             max_sum = current_sum
#     return max_sum
# print(max_sum_k(arr,k))

# #level 2
# a = "abcabcbb"

# def longest_unique_substring(a):
#     left = 0
#     best = 0
#     hashmap = {}
#     for right in range(len(a)):
#         hashmap[a[right]] = hashmap.get(a[right], 0) + 1
#         while hashmap.get(a[right]) > 1:
#             hashmap[a[left]] = hashmap.get(a[left],0) - 1
#             left += 1
#         best = max(best, right-left+1)
#     return best
# print(longest_unique_substring(a))

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

# string = "eceba"
# def k_distinct(s, k):
#     freq = {}
#     best = 0
#     left = 0
#     for i in range(len(s)):
#         freq[s[i]] = freq.get(s[i], 0) +1
#         while len(freq) > k:
#             freq[s[left]]-=1
#             if freq[s[left]] == 0:
#                 del freq[s[left]]
#             left+=1
#         best = max(best, i - left + 1)
#     print(best)
# k_distinct(string, 2)


# a = "eceba"
# k = 2 
# def longest_substriing(a,k):
#     l = 0
#     n = len(a)
#     best = 0
#     freq= {}
#     for r in range(n):
#         freq[a[r]] = freq.get(a[r],0) + 1
#         while len(freq) > k:
#             freq[a[l]] = freq.get(a[l], 0) - 1
#             if freq[a[l]] == 0:
#                 del freq[a[l]]
#             l += 1
#         best = max(r-l+1, best)
#     return best
# print(longest_substriing(a,k))

s = "aaaabbccc"
# s = 'aa'
k = 2
def longest_exact_k(s,k):
    l = 0
    n = len(s)
    best = 0
    freq= {}
    for r in range(n):
        freq[s[r]] = freq.get(s[r], 0) + 1
        while len(freq) > k:
            freq[s[l]] = freq.get(s[l], 0) - 1
            if freq[s[l]] == 0:
                del freq[s[l]]
            l+=1
        if len(freq) < k:
            best = 0
        else:
            best = max(best, r-l+1)
        # if len(freq) == k:
        #     best = max(best, r - l + 1)
    return best
print(longest_exact_k(s, k))


string = "eceba"
k =2 
# def distinc_values(s, k):
#     left = 0
#     n = len(s)
#     freq = {}
#     best = 0
#     for right in range(n):
#         freq[s[right]] = freq.get(s[right],0) + 1
#         while len(freq) > k:
#             freq[s[left]] = freq[s[left]] -1
#             if freq[s[left]] == 0:
#                 del freq[s[left]]
#             left+=1
#         best = max(best, right-left+1)
#     print(best)


a = [2,1,3,2,4,1,1]
# a = [7]
k = 7
def longest_k_sum_sub_arr(a, k):
    left = 0 
    pairs = 0 
    total_sum = 0
    for i in range(len(a)):
        total_sum+= a[i]
        while total_sum > k:
            total_sum -= a[left]
            left+=1
        pairs = max(pairs, i-left+1)

    print(pairs)
# def longest_k_sum_sub_arr(a, k):
#     left = 0
#     total_sum =0
#     total_pair = 1
#     max_total_pair = 1
#     for right in range(1,len(a)):
#         sum_pair = a[right]+ a[right-1]
#         if total_sum+ sum_pair <=k:
#             total_pair+= 1
#             total_sum += sum_pair
#         else:
#             total_sum -= a[left]
#             left += 1
#             max_total_pair = max(max_total_pair, total_pair)
#             total_pair = 1
#     print(max(max_total_pair, total_pair))

longest_k_sum_sub_arr(a,k)


string = "eceba"
k =2 
def distinc_values (s, k):
    left = 0
    freq = {}
    max_pairs = 0
    for right in range(len(s)):
        freq[s[right]] = freq.get(s[right], 0)+1
        while len(freq) > k:
            freq[s[left]] -=1
            if freq[s[left]] == 0:
                del freq[s[left]]
            left +=1
        max_pairs = max(max_pairs, right-left+1)
    print(max_pairs)
    
distinc_values(string,k)

a = [2,1,3,2,4,1,1]
# a = [7]
k = 7
def longest_k_substring(a, k):
    left = 0
    max_pair = 0
    total_sum = 0
    for right in range(len(a)):
        total_sum += a[right]
        while total_sum > k:
            total_sum -= a[left]
            left +=1
        max_pair = max(max_pair, right-left+1)
    return max_pair
print(longest_k_substring(a, k))