
def solve(inputs, arr):
    output = []
    largest = 0
    for i in range(inputs[0]):
        for j in range(i, inputs[1]):
            if arr[j] > largest:
                largest = arr[j]
        output.append(largest)

    for i in output:
        print(i, end=" ")


user_input = list(map(int, input().split()))
arr = list(map(int, input().split()))

print(solve(user_input, arr))