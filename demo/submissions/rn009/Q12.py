def validity(a,b):
    vala=valb=0
    i=0
    while(True):
        if (len(a[i])!=len(a[i-1])):
            vala = 1
            break
        else:
            i+=1
    j=0
    while(True):
        if (len(b[j])!=len(b[j-1])):
            valb = 1
            break
        else:
            j+=1

    if(vala == 0 and valb ==0):
        if (len(a) == len(b[0])):
            return 0
        else:
            return 1

def matmul(a,b):
    c=[]
    if (validity==1):
        return 0
    if (validity == 0):
        for i in range(len(a)):
            c.append(0) 
            for j in range(len(b[0])):
                c[i].append(0)
                for k in range(len(b)):
                    c[i][j] += a[i][k] * b[k][j]
    return c


if __name__ == "__main__":
    res= matmul([[1 , 2 , 3] , [4 , 5 , 6]] , [[7 , 10] , [8 , 11] , [9 , 12]])
    print(res)


