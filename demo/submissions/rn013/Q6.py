def ndiamond(n):
    i = 0
    # In the ascending pattern, i varies from 0 to (n+1)//2
    for i in range(0, (n+1)//2):
        j = 0
        for j in range(0, n//2 - i ): # j iterates through total  number of spaces to be printed
            print(" ", end = "")

        k = 1
        while(k <= (2*i + 3)//2):
            print(k, end = "")
            k += 1
        k = k - 2     # since value increases at first, then decreases in a single row
        while(k >= 1):
            print(k, end = "")
            k -= 1
        print("")
    i = i - 1       # to print the descending part of the diamond
    while(i >= 0):
        j = 0
        for j in range(0, n // 2 - i):
            print(" ", end="")

        k = 1
        while (k <= (2 * i + 3) // 2):  # according to pattern, max value of k is (2*i + 3)//2
            print(k, end="")
            k += 1
        k = k - 2
        while (k >= 1):
            print(k, end="")
            k -= 1
        print("")
        i -= 1

if __name__ == "__main__":
    a = int(input())
    ndiamond(a)




