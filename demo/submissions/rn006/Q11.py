def mattrans(m):
  row1=len(m)
  col1=len(m[0])
  b=[[0 for i in range(row1)] for j in range(col1)]
  for i in range(row1):
    for j in range(col1):
      b[j][i]=m[i][j]
  return(b)


if (__name__=="__main__"):
  m=[]
  row=int(input("Enter number of rows "))
  colm=int(input("Enter number of columns "))

  for i in range(row):
    a=[]
    for j in range(colm):
      a.append(int(input()))
    m.append(a)
  print(mattrans(m))
