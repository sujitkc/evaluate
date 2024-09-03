def diamond():
    a=2
    b=1
    for i in range (3):
        for j in range (a):
            print(" ",end='')
        for k in range (b-1):
            print ("*",end='')
        print("*")
        b=b+2
        a=a-1
    if(b>=5):
        b=3
        a=1
    for i in range (2):
        for j in range (a):
            print(" ",end='')
        for k in range (b-1):
            print ("*",end='')
        print("*")
        b=b-2
        a=a+1
if __name__=="__main__":
    diamond()