# Solution for second question.

#(a)
def increment(x):
    return (x+1)
    
def decrement(x):
    return (x-1)

#(b)
def add(x,y):
    if(y>0):
        for i in range(y):
            x = increment(x)    
    else:
        for i in range(-y):
            x=decrement(m)
        return(m)
            
def subtract(x,y):
    if(y>0):
        for i in range(y):
            x = decrement(x)
    else:
        for i in range(-y):
            x = increment(x)
    return(x)    
        
#(c) 
def multiply(x,y):
    s = 0
    for i in range(y):
        s = add(s,x)
    return (s)
        
def divide(x,y):
    c = 0
    while(x>=y):
        x = subtract(x,y)
        c = c+1
    return c
    
#(d)
def exponent(x,y):
    p = 1
    for i in range(y):
        p = multiply(p,x)
    return p
