def double(l):
    lst=[]
    for i in range(len(l)):
        lst.append(2*l[i])
    return (lst)    
if __name__=="__main__":
    l=[int(x) for x in input().split(",")]
    print(double(l))
