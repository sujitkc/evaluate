def diamond():
    for i in range(5):
        if(i<3):
            for _ in range(i,2):
                print(" ", end=" ")
            for _ in range(2*i,-1,-1):
                print("*", end=" ")
        elif(i>=3):
            for _ in range(i,2,-1):
                print(" ", end=" ")
            for _ in range(2*i,9):
                print("*", end=" ")
        print("")

if(__name__=="__main__"):
    diamond()

