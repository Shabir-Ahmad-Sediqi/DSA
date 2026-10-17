
def palindrome(text):
    return True if text == text[::-1] else False
    

text = input()
print(palindrome(text))