



def twoSum(arr, target):

    L = len(arr)

    for i in range(L):
        for j in range(i+1, L):
            if arr[i] + arr[j] == target:
                return arr[i], arr[j]
    return []

arr = list(map(int, input().split()))
target = int(input())
print(twoSum(arr, target))

