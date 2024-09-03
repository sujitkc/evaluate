def diamond():
    n = 5
    c = "*"
    i = 1
    while i <= ((n-1)/2):
        k = int(((n+1)/2)-i)
        for j in range(k):
            print(" ", end="")
        for j in range((2*i)-1):
            print(c, end="")
        print("")
        i += 1
    for x in range(n):
        print(c, end="")
    print("")

    t = int((n-1)/2)
    while t > 0:
        k = int(((n + 1) / 2) - t)
        for j in range(k):
            print(" ", end="")
        for j in range((2*t) - 1):
            print(c, end="")
        print("")
        t -= 1


if __name__ == "__main__":
    diamond()
