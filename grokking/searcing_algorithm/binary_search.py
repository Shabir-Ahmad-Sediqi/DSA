
# def binarySearch(arr, left, right, target):

#     while left <= right:
#         mid = (left + right) // 2
#         if arr[mid] == target:
#             return target
#         elif arr[mid] < target:
#             left = mid + 1
#         else:
#             right = mid - 1 
    

# # print(binarySearch(arr, left, right, target)) 

# # Bnary search with recursion

# def binarySearchWithRecursion(arr, left, right, target):
#     if left > right:
#         return "Not Found"
#     mid = (left + right) // 2
#     if arr[mid] == target:
#             return target
#     elif arr[mid] < target:
#          return binarySearchWithRecursion(arr, mid + 1, right, target)
#     else:
#          return binarySearchWithRecursion(arr, left, mid - 1, target)

# arr = [2,5,3,8,6,0,1]
# arr.sort()
# print(arr)
# target = 6
# left = 0
# right = len(arr) - 1         

# print(binarySearchWithRecursion(arr, left, right, target))


def binarrySearch(arr, target):

     left = 0
     right = len(arr) - 1
     while left <= right:
          mid = (left + right) // 2
          if arr[mid] == target:
               return target
          elif arr[mid] > target:
               right = mid - 1
          else:
               left = mid + 1

arr = [2,4,1,5,6,3]
sorted_arr = sorted(arr)
target = 6
print(binarrySearch(sorted_arr, target))