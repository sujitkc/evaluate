def diamond(n):
    for i in range(1, int(n/2+1)):
        print(" "*int((n+1)/2 - i) + str(int("1"*i)**2))
    for i in range(int(n/2+1), 0, -1):
        print(" "*int((n+1)/2 - i) + str(int("1"*i)**2))

