def matmul(A,B):
    rowsofA=len(A)
    colsofA=len(A[0])
    rowsofB=len(B)
    colsofB=len(B[0])

    if(colsofA != rowsofB):
        print("Cannot Multiply the two matrices")

    else:
        C=[[0 for row in range(colsofB)] for col in range(rowsofA)]
        for i in range(rowsofA):
            for j in range(colsofB):
                for k in range(colsofA):
                    C[i][j] += A[i][k]*B[k][j]

        return C

if __name__ == "__main__":
    print(matmul([[1,2,3],[4,5,6]],[[7,10],[8,11],[9,12]]))
    
