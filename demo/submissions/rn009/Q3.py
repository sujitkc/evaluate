def banner(m):
    for _ in range(len(m)+4):
        print("*", end="")
    print("\n*",m,"*")
    for _ in range(len(m)+4):
        print("*", end="")
if (__name__=="__main__"):
    m=input()
    banner(m)