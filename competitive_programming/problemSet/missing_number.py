
def missing_number(n, arr):


    total_sum = (n * (n + 1)) // 2
    sum_of_arr = sum(arr)
    return total_sum - sum_of_arr



n = int(input())
arr = list(map(int, input().split()))
print(missing_number(n, arr))