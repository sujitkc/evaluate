def diamond():
    # replacing n with 5 in Q4b
    i = 0
    for i in range(0, 3):
        j = 0
        for j in range(0, 2 - i ):
            print(" ", end = "")

        k = 0
        while(k < (2*i + 1)):
            print("*", end = "")
            k += 1
        print("")
    i = i - 1
    while(i >= 0):
        j = 0
        for j in range(0, 2 - i):
            print(" ", end="")

        k = 0
        while (k < (2 * i + 1)):
            print("*", end="")
            k += 1
        print("")
        i -= 1

if __name__ == "__main__":
    diamond()

