
def bubbleSort(array):
    for i in range(len(array)):
        for j in range(len(array)-1):
            if array[j] > array[j + 1]:
                array[j],array[j+1] = array[j+1],array[j]
    return array

arr = [3,2,4,1,5]

print(bubbleSort(arr))
