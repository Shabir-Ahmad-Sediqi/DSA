
def searchInsert(nums, target) -> int:
    
    left = 0
    right = len(nums)

    while left <= right:
        mid = (left + right) // 2

        if nums[mid] == target:
            return mid
        elif nums[mid] + 1 == target:
            return mid + 1
        elif nums[mid] > target:
            right = mid - 1
        else:
            left = mid + 1

target = 7
arr = [2, 3 ,1, 5 ,6]
arr.sort()
print(arr)
print(searchInsert(arr, target))
