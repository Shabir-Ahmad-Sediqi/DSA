
def validSubsequence(arr, subArr):

    for i in subArr:
        if i in arr:
            continue
        else:
            return False
    return True

arr = list(map(int, input().split()))
subArr = list(map(int, input().split()))

print(validSubsequence(arr, subArr))