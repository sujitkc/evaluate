def diamond(n):
    for i in range(n):
        if(i<(n+1)/2):
            for _ in range(i,int((n-1)/2)):
                print(" ", end=" ")
            for _ in range(2*i,-1,-1):
                print("*", end=" ")
        elif(i>=(n+1)/2):
            for _ in range(i,int((n-1)/2),-1):
                print(" ", end=" ")
            for _ in range(2*i,2*n-1):
                print("*", end=" ")
        print("")

if(__name__=="__main__"):
    n=int(input())
    diamond(n)

