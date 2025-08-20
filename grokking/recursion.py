# Recursion
# Is a concept where a function call itself, it has two properties
#  1. Base case -> for stoping the function call otherwise we'll get to an
# infinte loop
# 2. Recursive case -> where we keep calling the function until it meets the base case

#Note: Recursion uses Stack Data Structure

# Attention!
# To better understand recursion I'll do an example if Factorial.

def factorial(number):
    # Base case here
    if number < 2:
        return 1
    else:
        # Recursive case where we keep calling the function again and again
        # for smaller value
        return number * factorial(number - 1)
    
print(factorial(5)) # Answer -> 5 * 4 * 3 * 2 * 1 = 120

# Exercise count number of item in a list using recursion

def count(items):
    if len(items) == 0: return 0
    items.pop()
    return 1 + count(items)

items = [2,3,4,5]
print(len(items))
print(count(items))