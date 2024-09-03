def even_elements(l):
    l=[a for a in l if int(a)%2==0]
    return l

if __name__ == "__main__":
    l=input().split(", ")
    out = even_elements(l)
    print(out)