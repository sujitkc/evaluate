def diamond(n):
    i = 0
    for i in range(0, (n+1)//2): # according to pattern for the ascending part of diamond
        j = 0
        for j in range(0, n//2 - i ):  # code to print spaces
            print(" ", end = "")

        k = 0
        while(k < (2*i + 1)):       # code to print character
            print("*", end = "")
            k += 1
        print("")
    i = i - 1          # according to pattern for the descending part of diamond
    while(i >= 0):
        j = 0       # code to print spaces
        for j in range(0, n // 2 - i):
            print(" ", end="")

        k = 0       # code to print characters
        while (k < (2 * i + 1)):
            print("*", end="")
            k += 1
        print("")
        i -= 1






