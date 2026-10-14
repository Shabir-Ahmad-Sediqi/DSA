from collections import defaultdict

# This was the efficiant way of solving it. at the first solution i poped the value the from  

def secondSolution(text):

    count = defaultdict(int)

    for i in text:
        count[i] += 1

    for index, char in enumerate(text):
        if count[char] == 1:
            return index
    print(count)
    return -1 

text = input().lower()
print(secondSolution(text))

# better Approach

