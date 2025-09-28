
def longest_substring(s: str) -> int:
    count = 1
    count_hash = {}

    for char in range(len(s)-1):
        if s[char] == s[char + 1]:
            count += 1
        else:
            count_hash[char] = count
            count = 1
    count_hash[s[::-1]] = count

    max_value = max(count_hash.values())
    return max_value

s = input()

print(longest_substring(s))