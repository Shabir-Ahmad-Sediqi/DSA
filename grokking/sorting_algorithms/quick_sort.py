# Quick Sort is a divide and conquer algorithm:

# Pick a pivot element from the array.

# Partition the array into:

# Left: elements smaller than pivot.

# Right: elements greater than pivot.

# Recursively apply the same steps to left and right subarrays.

# Combine results → sorted array.

# Code --> 

def quickSort(arr):
    # Base case if length of array is less then 2, it means either its empty or 1 element, already sorted
    if len(arr) < 2:
        return arr
    pivot = arr[len(arr)//2] # Select pivot always from middle of the array
    # get the left hand side array smaller than pivot
    left = [i for i in arr if i < pivot]
    # get the right hand side array bigger than pivot
    right = [i for i in arr if i > pivot]
    return quickSort(left) + [pivot] + quickSort(right)

arr = [3,2,6,7,4,8,6,0,1,]
print(quickSort(arr))
