def is_wellformed(mata):
 count=len(mata[0])
 for i in range(len(mata)):
   if count==len(mata[i]):
     k=1
   else: 
     k=0
 return(bool(k))

def are_addable(mat1b,mat2b):
   if (len(mat1b[0]))==(len(mat2b[0])):
     anss=1
   else:
     anss=0
   if (is_wellformed(mat1b)==1 and is_wellformed(mat2b)==1 and anss == 1):
     return("True")
   else:
     return("False")

def are_multipliable(mat1c,mat2c):
  if len(mat1c[0])==len(mat2c):
    k=1
  else:
       k=0
  if (is_wellformed(mat1c)==1 and is_wellformed(mat2c)==1 and k == 1):
    return("True")
  else:
    return("False")

def scalar_multiply_list(n,lstd):
  lans=[]
  for i in range(len(lstd)):
    lans.append(n*lstd[i])
  return lans

def  scalar_multiply_matrix(n,mate):
  lansf=[]
  for lstt in mate:
    lansf.append(scalar_multiply_list(n,lstt))
  return(lansf)
  
def add_lists(mat1f,mat2f):
  lans=[]
  for i in range(len(mat1f)):
    lans.append(mat1f[i]+mat2f[i])
  return(lans)

def add_matrices(mat1g,mat2g):
  lansf=[]
  if are_addable(mat1g,mat2g)=="True":
    for i in range(len(mat1g)):
     lansf.append(add_lists(mat1g[i],mat2g[i]))
    return([lansf[0]])
  else: 
     return("Not Possible")

def multiply_lists(lst1h,lst2h):
  lans=[]
  for i in range(len(lst1h)):
    lans.append(lst1h[i]*lst2h[i])
  return(lans)

def transpose(mat2i):
  lans=[]
  for j in range(len(mat2i[0])):
    lans.append([])
  for i in range(len(mat2i)):
    for k in range(len(mat2i[0])):
      lans[k].append(mat2i[i][k])
  return(lans)

def multiply_matrices(mat1j,mat2j):
  if are_multipliable(mat1j,mat2j)!="True":
    return("Not Possible")
  else: 
    lansp=[]
    mat2t=transpose(mat2j)
    for i in range(len(mat1j)):
      lansp.append([])
      for j in range(len(mat2j[0])):
        k=multiply_lists(mat1j[i],mat2t[j])
        ans=0
        for el in k:
          ans=el+ans
        lansp[i].append(ans)
    return(lansp)
    
    
if __name__ == "__main__":
  print ( is_wellformed ([[1 , 2 , 3] , [20 , 40 , 50]]))
  print ( is_wellformed ([[1 , 2 , 3] , [20 , 40]]))
  print ( are_addable ([[1 , 2 , 3] , [20 , 40 , 50]] , [[1 , 2 , 3] , [20 , 40 , 50]]))
  print ( are_addable ([[1 , 2] , [20 , 40]] , [[1 , 2 , 3] , [20 , 40 , 50]]))
  print ( are_multipliable ([[1 , 2 , 3] , [20 , 40 , 50]] , [[1 , 2 , 3] , [20 , 40 , 50]]))
  print ( are_multipliable ([[1 , 2] , [20 , 40]] , [[1 , 2 , 3] , [20 , 40 , 50]]))
  print ( scalar_multiply_list (3 , [1 , 2 , 3]))
  print ( scalar_multiply_matrix(3 , [[1 , 2 , 3]]))
  print ( add_lists ([1 , 2 , 3] , [4 , 5 , 6]))
  print ( add_matrices ([[1 , 2 , 3]] , [[4 , 5 , 6]]))
  print ( multiply_lists ([1 , 2 , 3] , [4 , 5 , 6]))
  print ( multiply_matrices ([[1 , 2 , 3] ,[4 , 5 , 6]] ,[[7 , 10] , [8 , 11] , [9 , 12]]))
  
   
  
