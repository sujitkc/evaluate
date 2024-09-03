def ndiamond():
    n=5
    space=int((n-1)/2)#for spaces
    number=1#for printing numbers
    a=int((n+1)/2)
    for i in range (a):#for upper half of diamond
        for i in range(space):
            print(" ",end="")
        for j in range (1,number+1):#left part of diamond
            print(j,end="")
        for k in range (number-1,0,-1):#right part of diamond
            print(k,end="")
        print("")
        space=space-1#necessary changes to loop counter
        number =number+1
    if(space==-1):#for lower half of diamond
        space=1#necessary changes to loop counter
        number=number-2
        for i in range(a-1):
            for i in range (space):
                print(" ",end="")
            for j in range (1,number+1):#lest part of diamond
                print(j,end="")
            for k in range (number-1,0,-1):#right part of diamond
                print(k,end="")
            print()
            space=space+1
            number=number-1
if __name__=="__main__":
    ndiamond()