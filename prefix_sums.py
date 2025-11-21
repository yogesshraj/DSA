# a = [3, 7, 5, 10, 9, 11]
# a = [1, 2, 3, 4]
a = [5, 6, 7, 8, 1, 2, 3, 4, 5]
def longest_inc_subarray(arr):
    max_value = 1
    overall_best = 1
    for i in range(1, len(arr)):
        if arr[i] > arr[i-1]:
            max_value +=1 
        else:
            overall_best = max(overall_best, max_value)
            max_value = 1
    print(max(overall_best, max_value))

longest_inc_subarray(a)

#proper prefix sum
a = [2,1,3,2]
def prefix_sum_arr(a):
    prefix_sum = [0]
    for i in range(len(a)):
        prefix_sum.append(prefix_sum[-1]+a[i])
    return prefix_sum
prefix_sum = prefix_sum_arr(a)
print(prefix_sum)
#find sum first three elements.
print(prefix_sum[3]- prefix_sum[0])

c = [5,6,7,73,26]
def prefix_sums(c):
    return_arr = [0]
    for i in c:
        return_arr.append(return_arr[-1]+i)
    return return_arr
prefix_sum_man = prefix_sums(c)
print(prefix_sum_man[5]- prefix_sum_man[2])


a = [1, 2, 3, -1, 2]
k = 3
def prefix_sum_for_exact_k_values(a, k):
    prefix_sum_array = [0]
    for i in range(len(a)):
        prefix_sum_array.append(prefix_sum_array[-1]+ a[i])
    
    print(prefix_sum_array)
prefix_sum_for_exact_k_values(a,k)
