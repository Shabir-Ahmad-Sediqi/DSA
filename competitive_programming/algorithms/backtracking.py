from itertools import permutations

nums = [1,2,3]

print(list(permutations(nums)))

def permutation(nums):

    result = []
    current = []
    chosen = [False, False, False]

    def backtrack():
        if len(current) == len(nums):
            result.append(current.copy())
            return
        
        for i, num in enumerate(nums):
            if chosen[i]:
                continue
            chosen[i] = True
            current.append(num)
            backtrack()
            chosen[i] = False
            current.pop()

    backtrack()
    return result

# print(permutation([1,2,3]))



































