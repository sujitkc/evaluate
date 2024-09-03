def ndiamond(n):
    if(n%2!=0):
        space=int((n-1)/2)# for spaces
        number=1
        a=int((n+1)/2)
        for i in range (a):#upper half
            for i in range(space):
                print(" ",end="")
            for j in range (1,number+1):#left part
                print(j,end="")
            for k in range (number-1,0,-1):#right part
                print(k,end="")
            print("")
            space=space-1
            number =number+1
        if(space==-1):
            space=1
            number=number-2
            for i in range(a-1):#lower half
                for i in range (space):
                    print(" ",end="")
                for j in range (1,number+1):#left part
                    print(j,end="")
                for k in range (number-1,0,-1):#right part
                    print(k,end="")
                print()
                space=space+1
                number=number-1
if __name__=="__main__":
    n=int(input())
    ndiamond(n)