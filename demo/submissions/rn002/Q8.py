def double(l):
    l1=[2*x for x in l]
    return l1

if __name__ == "__main__":
    l=[]
    str=input()
    l=[int(n) for n in str.split(",")]
    print(double(l))
