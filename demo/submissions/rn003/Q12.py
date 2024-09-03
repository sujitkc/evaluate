def matmul(M1,M2):
    if(len (M1[0])==len(M2)):#condition for multiplication of matrices
        M=[]
        for i in range (len(M1)):#to make a zero matrix of appropriate dimensions
            m=[0*j for j in range (len(M2[0]))]
            M.append(m) 
        for rownum in range (len(M1)):
            for colnum in range(len(M2[0])):
                for i in range(len(M1[0])):
                    M[rownum][colnum]+=M1[rownum][i]*M2[i][colnum]#condition for calculating some elements of matrix from 0 to appropriate value
        return(M)
    else:
        print("error")
if __name__=="__main__":
    t=matmul([[1,2],[3,4]],[[2,0],[1,2]])
    print(t)