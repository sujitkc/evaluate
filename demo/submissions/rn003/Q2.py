def increment(n):
    return n+1
def decrement(n):
    return n-1
def add(n,m):
    for i in range(m):
        n=increment(n)
    return n
def subtract(n,m):
    for i in range(m):
        n=decrement(n)
    return n
def multiply(a,b):
    product=0
    for i in range(b):
        product+=a
    return product
def divide(a,b):
    quotient=0
    while(a>b):
        a-=b
        quotient+=1
    return quotient
def exponent(n,m):
    exponent=1
    for i in range(m):
        exponent*=n
    return exponent
if __name__=="__main__":
    print(increment(1))
    print(decrement(1))
    print(add(50,51))
    print(subtract(4,7))
    print(multiply(5,6))
    print(divide(-2,3))
    print(exponent(2,10))
