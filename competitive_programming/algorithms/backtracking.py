
n = 3
permutation = []
chosen = [False,False,False]

def search():
    if len(permutation) == n:
        print(permutation)
    else:
        for i in range(n):
            if chosen[i]:
                continue
            chosen[i] = True
            permutation.append(i)
            search()
            chosen[i] = False
            permutation.pop()

search()