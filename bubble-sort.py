def bubbleSort(array):
    L = len(array)-1
    for i in range(L):
        for j in range(L):
            if array[j] > array[j+1]:
                array[j+1],array[j] = array[j], array[j+1]
    return array

array = [3,2,4,1,5]
print(bubbleSort(array))