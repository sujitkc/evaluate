def matmul(m1,m2):
  row1=len(m1)
  col1=len(m1[0])
  row2=len(m2)
  col2=len(m2[0])
  m=[[0 for i  in range(col2)] for j in range(row1)]
  if(col1==row2):
    for i in range(row1):
      for j in range(col2):
        for k in range(row2):
          m[i][j] += m1[i][k]*m2[k][j]
    return(m)
  else:
    return("Error")


if(__name__=="__main__"):
  m1=[]
  row1=int(input("Enter number of rows "))
  colm1=int(input("Enter number of columns "))
  for i in range(row1):
    a1=[]
    for j in range(colm1):
      a1.append(int(input()))
    m1.append(a1)

  m2=[]
  row2=int(input("Enter number of rows "))
  colm2=int(input("Enter number of columns "))
  for i in range(row2):
    a2=[]
    for j in range(colm2):
      a2.append(int(input()))
    m2.append(a2)

  print(matmul(m1,m2))
