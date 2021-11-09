def increment(x):
    return (x+1)

def decrement(x):
    return (x - 1)

def add(x, y):
    i = 0
    for i in range(0, y):
        x = increment(x)  # performing x = x + 1 using increment()
    return x

def subtract(x, y):
    i = 0
    for i in range(0, y):
        x = decrement(x)  # performing x = x - 1 using decrement()
    return x

def multiply(x, y):
    i = 0
    z = 0
    for i in range(0, y):
        z = add(x, z)
    return z

def divide(x, y):
    i = 0
    while (x > y):
        x = subtract(x, y)  # repeatedly subtracting y from x and returning the number of times of repeated subtraction as the quotient.
        i+=1
    return i

def exponent(x, y):
    i = 0
    z = 1
    for i in range (0, y):
        z = multiply(x, z)
    return z

if __name__ == "__main__":
    print(increment(1))
    print(decrement(1))
    print(add(1, 2))
    print(subtract(1, 2))
    print(multiply(3, 7))
    print(divide(9, 2))
    print(exponent(2, 7))


