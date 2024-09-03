def mattrans(mat):
  ans=[]
  for i in range(c): 
    ans.append([]) 
    for j in range(r): 
      ans[i].append(0)    
  for i in range(r):
    for j in range(c):
      ans[j][i] = mat[i][j]
  print(ans)
  
if __name__ == "__main__":

  r = int(input("type in the row limit(>0): "))
  c=  int(input("type in the cloumn limit(>0): "))
  mat=[]
  for i in range(r): 
    mat.append([]) 
    for j in range(c): 
      x=int(input("type in the element: "))
      mat[i].append(x)
  
  mattrans(mat)
