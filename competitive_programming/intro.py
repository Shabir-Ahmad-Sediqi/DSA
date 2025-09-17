
# Same as c++ when input is not determined

while True:
    try:
        text = input()
    except EOFError:
        break

