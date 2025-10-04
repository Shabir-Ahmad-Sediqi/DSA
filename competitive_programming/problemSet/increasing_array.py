
def solve(n ,arr):
    count = 0
    for i in range(n-1):
        if arr[i] > arr[i+1]:
            diffrence = arr[i] - arr[i+1]
            arr[i+1] += diffrence
            count += diffrence
    
    return count

n = int(input())
arr  = list(map(int, input().split()))

print(solve(n, arr))