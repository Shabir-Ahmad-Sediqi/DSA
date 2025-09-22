
def maxSubAarraySum(array):
    sum_subarray= 0
    best = 0

    for i in array:
        sum_subarray= max(i, i + sum_subarray)
        best = max(best, sum_subarray)

    return best

array = [-1, 2, 4, -3, 5, 2, -5, 2]
print(maxSubAarraySum(array))
