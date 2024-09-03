def even_elements(l):
    lst=[]
    for i in range(len(l)):
        l[i]=int(l[i])
        if(l[i]%2==0):
            lst.append(l[i])
    return(lst)
if __name__=="__main__":
    #l=[int(x) for x in input().split(",")]
    l=input().split(",")
    print(even_elements(l))