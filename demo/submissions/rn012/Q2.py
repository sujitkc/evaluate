def increment(n):
    return n+1

def decrement(n):
    return n-1

def add(n,m):
    k=n
    i=0
    if m>0:
        while i<m:
            k=increment(k)
            i=increment(i)
    else:
        while i<-m:
            k=decrement(k)
            i=increment(i)
    return k

def subtract(n,m):
    k=n
    i=0
    if m>0:
        while i<m:
            k=decrement(k)
            i=increment(i)
    else:
        while i<-m:
            k=increment(k)
            i=increment(i)
    return k

def multiply(n,m):
    i=0
    k=0
    while i<m:
        k=add(k,n)
        i=increment(i)
    return k

def divide(n,m):
    i=n
    k=0
    while i>m:
        k=increment(k)
        i=subtract(i,m)
    return k

def exponent(n,m):
    i=0
    k=1
    while i<m:
        k=multiply(k,n)
        i=increment(i)
    return k
