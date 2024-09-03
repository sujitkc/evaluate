
def diamond(n, c):
    for i in range(0, n, 2):
        print(" "*int((n-i-1)/2) + c*(i + 1))
    for i in range(n - 1, 0, -2):
        print(" "*int((n-i+1)/2) + c*(i - 1))

