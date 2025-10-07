
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