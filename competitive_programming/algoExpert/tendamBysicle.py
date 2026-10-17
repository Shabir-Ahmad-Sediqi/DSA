def solution(red, blue, fastest):

    input = """
    5, 5, 3, 9, 2
    3, 6, 7, 2, 1
    True
    """

    L = len(blue)

    if fastest == True:
        red.sort()
        blue.sort(reverse=True)

    else: 
        red.sort()
        blue.sort()

    max_sum = 0

    for i in range(L):
        result = max(red[i], blue[i])
        max_sum += result
    return max_sum

red = list(map(int, input().split(", ")))
blue = list(map(int, input().split(", ")))
fastest = bool(input())

print(solution(red, blue, fastest))