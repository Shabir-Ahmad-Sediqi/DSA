
subset = []

def search(k,n):
    if k == n:
        print(subset)
        return 
    search(k+1,n)
    subset.append(k)
    search(k+1,n)
    subset.pop()

n = int(input())

search(0,n)

# bit representation

#  n = int(input("Enter n: "))

for b in range(1 << n):  # from 0 to 2^n - 1
    subset = []
    for i in range(n):
        if b & (1 << i): # checks if element i is in subset
            subset.append(i)
    print(subset)
