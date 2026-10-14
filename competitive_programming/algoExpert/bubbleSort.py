
def bubbleSort(arr):

    L = len(arr)

    for i in range(L):

        swapped = False

        for j in range(0, L-i-1):
            if arr[j] > arr[j+1]:
                arr[j],arr[j+1] = arr[j+1], arr[j]
                swapped = True
        if swapped == False:
            break
    return arr

arr = list(map(int, input().split()))
print(bubbleSort(arr))