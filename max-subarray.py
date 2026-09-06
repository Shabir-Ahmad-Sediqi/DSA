def subarray(arr):
    best = 0
    sam = 0
    length = len(arr)
    for i in range(length):
       sam = max(arr[i], sam+arr[i])
       best = max(best,sam)
    return best



arr = list(map(int, input().split()))

print(subarray(arr))