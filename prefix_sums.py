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