def ndiamond():
    i = 0
    # replacing n = 5 in the general form of the program ( Q6)
    for i in range(0, 3):
        j = 0
        for j in range(0, 2 - i ):
            print(" ", end = "")

        k = 1
        while(k <= (2*i + 3)//2):
            print(k, end = "")
            k += 1
        k = k - 2
        while(k >= 1):
            print(k, end = "")
            k -= 1
        print("")
    i = i - 1
    while(i >= 0):
        j = 0
        for j in range(0, 2 - i):
            print(" ", end="")

        k = 1
        while (k <= (2 * i + 3) // 2):
            print(k, end="")
            k += 1
        k = k - 2
        while (k >= 1):
            print(k, end="")
            k -= 1
        print("")
        i -= 1

