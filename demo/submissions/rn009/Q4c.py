def diamond(n,c):
    for i in range(n):
        if(i<(n+1)/2):
            for _ in range(i,int((n-1)/2)):
                print(" ", end=" ")
            for _ in range(2*i,-1,-1):
                print(c, end=" ")
        elif(i>=(n+1)/2):
            for _ in range(i,int((n-1)/2),-1):
                print(" ", end=" ")
            for _ in range(2*i,2*n-1):
                print(c, end=" ")
        print("")

if(__name__=="__main__"):
    n=int(input())
    c=input()
    diamond(n,c)

