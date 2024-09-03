def diamond(n, c):
    #  replacing '*' in Q4b with a general character c
    i = 0
    for i in range(0, (n+1)//2):
        j = 0
        for j in range(0, n//2 - i ):
            print(" ", end = "")

        k = 0
        while(k < (2*i + 1)):
            print(c, end = "")
            k += 1
        print("")
    i = i - 1
    while(i >= 0):
        j = 0
        for j in range(0, n // 2 - i):
            print(" ", end="")

        k = 0
        while (k < (2 * i + 1)):
            print(c, end="")
            k += 1
        print("")
        i -= 1

if __name__ == "__main__":
    n = int(input())
    c = str(input())
    diamond(n, c)