# def partition(array, low, high):
#     pivot = array[high]
#     i = low - 1
#     for j in range(low, high):
#         if array[j] <= pivot:
#             i += 1
#             array[i], array[j] = array[j], array[i]

#     print(array[i+1], array[high])
#     array[i+1], array[high] = array[high], array[i+1]
#     return i+1

# def quicksort(array, low, high):
#     if low < high:
#         pivot_index = partition(array, low, high)
#         quicksort(array, low, pivot_index-1) #left case
#         quicksort(array, pivot_index+1, high) #right case

# my_array = [64, 34, 25, 12, 22, 11, 90, 5]
# quicksort(my_array,0, len(my_array)-1)
# print("Sorted array:", my_array)



a = [5,87,3,64,7,3,75,86,3443,7,3,2,7,3133,7,4]
def partition(arr, low, high):
    pivot = arr[high]
    i = low - 1
    for j in range(low, high):
        if arr[j] < pivot:
            i+=1
            arr[i], arr[j] = arr[j], arr[i]
    arr[i+1], arr[high] = arr[high], arr[i+1]
    return i+1

def quicksort(arr, low, high):
    if low < high:
        pivot_index = partition(arr, low, high)
        quicksort(arr, low, pivot_index-1)
        quicksort(arr, pivot_index+1, high)
quicksort(a, 0, len(a)-1)
print(a)