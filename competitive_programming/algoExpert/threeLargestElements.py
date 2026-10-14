
def solution(arr):

    
    if len(arr) < 3:
        return []
    threeLargestNums = []

    j = 0

    while j < 3:

        largest = float('-inf')
        index = 0

        L = len(arr)
        for i in range(L):
            if arr[i] > largest:
                index = i
                largest = arr[i]
                

        arr.pop(index)
        threeLargestNums.append(largest)
        j += 1

    threeLargestNums.sort()
    return threeLargestNums

arr = list(map(int, input().split()))
print(solution(arr))