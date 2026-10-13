
def validSubsequence(arr, subArr):
    L = len(arr)
    j = 0

    for i in range(L):
        if arr[i] == subArr[j]:
            j += 1
        else:
            continue
    print(len(subArr))
    print(j)
    if j == len(subArr):
        return True
    else:
        return False
       
    

arr = list(map(int, input().split()))
subArr = list(map(int, input().split()))

print(validSubsequence(arr, subArr))