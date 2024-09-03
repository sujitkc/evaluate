def ndiamond(n):
    l=(n//2)+1
    i=l
    while(i>=1):
        s=1
        while(s<=i-1):
            print(" ",end="")
            s+=1
        inc=1
        while(inc<=l-i+1):
            print(inc,end="")
            inc+=1
        dec=l-i
        while(dec>=1):
            print(dec,end="")
            dec-=1
        print()
        i-=1
    l=n//2
    i=1
    while(i<=l):
        s=1
        while(s<=i):
            print(" ",end="")
            s+=1
        inc=1
        while(inc<=l-i+1):
            print(inc,end="")
            inc+=1
        dec=l-i
        while(dec>=1):
            print(dec,end="")
            dec-=1
        print()
        i+=1
if __name__=="__main__":
    n=int(input())
    ndiamond(n)
