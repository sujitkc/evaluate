def increment(x):
    return x+1
def decrement(x):
    return x-1
def add(a,b):
    for _ in range(b):
        a=increment(a)
    return a
def subtract(a,b):
    for _ in range(b):
        a=decrement(a)
    return a
def multiply(a,b):
    x=0
    for _ in range(b):
        x=add(x,a)
    return x
def divide(a,b):
    count=0
    x=a
    while (x>=b):
        x=subtract(x,b)
        count+=1
    return count
def exponent(a,b):
    x=a
    for _ in range(b):
        x=multiply(x,a)
        return x

if __name__ == "__main__":
    print(add(4,2),subtract(4,2),multiply(4,2),divide(4,2),exponent(4,2))