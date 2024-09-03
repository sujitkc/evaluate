def double(l):
    l=[int(a)*2 for a in l]
    return l

if __name__ == "__main__":
    l=input().split(", ")
    out = double(l)
    print(out)