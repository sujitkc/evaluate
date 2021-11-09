
def increment(x):
    return x+1

def decrement(x):
    return x-1

def add(x, y):
    for i in range(x):
        y = increment(y)
    return y

def subtract(x, y):
    for i in range(x):
        y = decrement(y)
    return y

def multiply(x, y):
    copy = 0
    for i in range(x):
        copy = add(copy, y)
    return copy

def division(x, y):
    copy = x
    for i in range(y):
        copy = subtract(copy, y)
    return copy

def exponent(x, y):
    copy = x
    for i in range(x):
        copy = multiply(x, copy)
    return copy




