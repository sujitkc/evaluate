def mattrans(M):
    T=[]    
    for colnum in range(len(M[0])):#to create a zero matrix whose elements will later be replaced to make transpose matrix
        m=[0*i for i in range (len(M))]
        T.append(m)
    #T=[[0,0],[0,0]]
    for rownum in range (len(M)):#for calculating transpose
        for colnum in range (len(M[0])):
            T[colnum][rownum]=M[rownum][colnum]
    return(T)
if __name__=="__main__":
    print(mattrans([[1,2],[3,4]]))
    M=[]
    x=int(input("no of rows=",))
    y=int(input("no of columns="))
    for i in range(x):
        m=[]
        M.append(m)
    for i in range(x):
        for j in range(y):
            M[i][j]=input().split(",")