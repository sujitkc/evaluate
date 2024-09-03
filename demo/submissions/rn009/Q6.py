def diamond(n):
    for i in range(n):
        if(i<(n+1)/2):
            for _ in range(i,int((n-1)/2)):
                print(" ", end="")
            for k in range(1,i+2):
                print(k, end="")
            for k in range(i,0,-1):
                print(k, end="")
        elif(i>=(n+1)/2):
            for _ in range(i,int((n-1)/2),-1):
                print(" ", end="")
            for k in range(i,n):
                print(k-i+1, end="")
            for k in range(n,i+1,-1):
                print(k-i-1, end="")
        print("")

if(__name__=="__main__"):
    n=int(input())
    diamond(n)

