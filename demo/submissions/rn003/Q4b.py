def diamond(n):
    if(n%2!=0):
        a=int((n-1)/2)
        d=int((n-1)/2)
        c=int((n+1)/2)
        b=1
        for i in range (c):
            for j in range (a):
                print(" ",end='')
            for k in range (b-1):
                print ("*",end='')
            print("*")
            b=b+2
            a=a-1
        if(b>=n):
            b=n-2
            a=1
        for i in range (d):
            for j in range (a):
                print(" ",end='')
            for k in range (b-1):
                print ("*",end='')
            print("*")
            b=b-2
            a=a+1
if __name__=="__main__":
    n=int(input())
    diamond(n)