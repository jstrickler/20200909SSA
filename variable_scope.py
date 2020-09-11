
x = 100  # GLOBAL variable

def spam():
    x = "Wolverine"
    print("in spam(): x is", x)
    y = 42  # LOCAL variable
    return x, y

values = spam()

print("values:", values)
print("x:", x)
