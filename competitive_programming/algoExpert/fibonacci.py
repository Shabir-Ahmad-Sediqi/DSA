
def fibonacci(n):

    if n == 0: return 0
    if n == 1: return 1

    sequence = [0,1]

    fib = fibonacci(n-1) + fibonacci(n-2)
    sequence.append(fib)
    return sequence[len(sequence)-1]

n = int(input())

print(fibonacci(n))