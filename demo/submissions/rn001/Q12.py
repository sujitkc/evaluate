def matmul(mat1,mat2):
  ans=[] 
  for i in range(c2): 
    ans.append([]) 
    for j in range(r1): 
      ans[i].append(0)
  for x in range(r1):
   for y in range(c2):
     for z in range(r2):
         ans[x][y] += mat1[x][z] * mat2[z][y]
  print(ans)    

if __name__ == "__main__":
  r1 = int(input("type in the row limit for matrice 1(>0): "))
  c1 = int(input("type in the column limit for matrice 1(>0): "))
  r2 = int(input("type in the row limit for matrice 2(>0): "))
  c2 = int(input("type in the column limit for matrice 2(>0): "))
  mat1=[]
  mat2=[]
  if (c1!=r2):
    print("Multiplication isnt possible")
  else: 
    for i in range(r1): 
      mat1.append([]) 
      for j in range(c1): 
        x=int(input("type in the element of mat1: "))
        mat1[i].append(x) 
    for i in range(r2): 
      mat2.append([]) 
      for j in range(c2): 
        x=int(input("type in the element of mat2: "))
        mat2[i].append(x)
        
  matmul(mat1,mat2)
