
def binarySearch(arr, left, right, target):

    while left <= right:
        mid = (left + right) // 2
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1 
    
arr = [2,5,3,8,6,0,1]
arr.sort()
print(arr)
target = 1
left = 0
right = len(arr) - 1
print(binarySearch(arr, left, right, target)) 