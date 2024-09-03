def matmul(A,B):
  row1=len(A)
  col1=len(A[0])
  row2=len(B)
  col2=len(B[0])
  if(col1 != row2):
    print("Cannot Multiply the two matrices")
  else:
    result=[[0 for row in range(col2)] for col in range(row1)]
    for i in range(row1):
      for j in range(col2):
        for k in range(col1):
          result[i][j] += A[i][k]*B[k][j] 
    return result

if __name__ == "__main__":
  a = [[1,2,3],[4,5,6]]
  b = [[7,10],[8,11],[9,12]]
  result = matmul(a,b)
  print(result)
    
