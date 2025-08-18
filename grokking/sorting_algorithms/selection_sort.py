
# Selecti0n sort is a classic algorithm for sorting as array of numbers.
# How it works!
# It select the smallest number in the current array and appends it to the new array 

# Function to find the smallest number
def findSmallestNumber(arr):
    smallestNum = arr[0] # suppose its the first element
    smallestIndex = 0
    for i in range(len(arr)):
        if smallestNum > arr[i]:
            smallestNum = arr[i]
            smallestIndex = i
    return smallestIndex

def selectionSort(arr):
    new_arr = []
    for i in range(len(arr)):
        smallest_index = findSmallestNumber(arr)
        new_arr.append(arr.pop(smallest_index))
    return new_arr

arr = [4,2,6,7,8,3,1]
print(selectionSort(arr))
