#DISCLAIMER
#there are many if name==main statements as I did not realize in the start that all of them had to be part 
# of same file instead of a,b,c... Thus I copy pasted them and this the result.I hope it is not a problem



def increment(x):

    return x+1

def decrement(y):
    return y-1


def add(x,y):

    for i in range(y):
        x=increment(x)

    return x

def subtract(x,y):

    for i in range(y):
        x=decrement(x)

    return x

if __name__ == "__main__":
    
    print(add(2,4))
    print(subtract(2,4))

def multiply(x,y):
    t=x

    if y==0:
        return 0

    for i in range(y-1):
        x=add(x,t)
        #print("x is:",x)

    return x

def divide(x,y):

    for i in range(y):
        if (subtract(x,y))>=0:

            x=subtract(x,y)
        else:
            x=0

    return x


if __name__ == "__main__":
    print(multiply(5,0))
    print(divide(7,2))


def exponent(x,y):
    t=x
    if y==0:
        return 1

    for i in range(y-1):

        x=multiply(x,t)

    return x

    
if __name__ == "__main__":
    print(exponent(2,0))




