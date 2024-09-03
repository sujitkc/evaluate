def diamond():
    for i in range(5):
        if(i<3):
            for _ in range(i,2):
                print(" ", end="")
            for k in range(1,i+2):
                print(k, end="")
            for k in range(i,0,-1):
                print(k, end="")
        elif(i>=3):
            for _ in range(i,2,-1):
                print(" ", end="")
            for k in range(i,5):
                print(k-i+1, end="")
            for k in range(5,i+1,-1):
                print(k-i-1, end="")
        print("")

if(__name__=="__main__"):
    diamond()

