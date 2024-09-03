
def diamond(n):
    for i in range(0, n, 2):
        print(" "*int((n-i-1)/2) + "*"*(i + 1))
    for i in range(n - 1, 0, -2):
        print(" "*int((n-i+1)/2) + "*"*(i - 1))

