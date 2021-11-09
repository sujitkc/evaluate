def is_wellformed(mat):
  a=len(mat[0])
  for row in range(len(mat)):
    b=len(mat[row])
    if(a is not b):
      return(False)
  return(True)


def are_addable(mat1,mat2):
  if(is_wellformed(mat1) and is_wellformed(mat2) and (len(mat1)==len(mat2)) and len(mat1[0])==len(mat2[0])):
    return(True)
  else:
    return(False)


def are_multipliable(mat1,mat2):
  if(is_wellformed(mat1) and is_wellformed(mat2) and len(mat1[0])==len(mat2)):
    return(True)
  else:
    return(False)


def scalar_multiply_list(n,lst):
  lst1=[]
  for i in range(len(lst)):
    lst1[i]=n*lst[i]
  return(lst1)


def scalar_multiply_matrix(n,mat):
  mat1=[[0 for i in range(len(mat[0]))] for j in range(len(mat))]
  for i in range(len(mat)):
    for j in range(len(mat[0])):
      mat1[i][j]=n*(int)(mat[i][j])
  return(mat1)


def add_lists(lst1,lst2):
  if(len(lst1)==len(lst2)):
    lst1=[(int)(x) for x in lst1]
    lst2=[(int)(x) for x in lst2]
    lst=[0 for i in range(len(lst1))]
    for i in range(len(lst1)):
      lst[i]=lst1[i]+lst2[i]
    return(lst)
  else:
    return("Error")


def add_matrices(mat1,mat2):
  if(not are_addable(mat1,mat2)):
    return("Error")
  mat=[[0 for i in range(len(mat1[0]))] for j in range(len(mat1))]
  for i in range(len(mat1)):
    mat[i]=add_lists(mat1[i],mat2[i])
  return(mat)


def multiply_lists(lst1,lst2):
  lst=[0 for i in range(len(lst1))]
  for i in range(len(lst1)):
    lst[i]=(int)(lst1[i])*(int)(lst2[i])
  return(lst)


def mattrans(m):
  row1=len(m)
  col1=len(m[0])
  b=[[0 for i in range(row1)] for j in range(col1)]
  for i in range(row1):
    for j in range(col1):
      b[j][i]=m[i][j]
  return(b)


def sum_of_list(lst):
  elem=0
  for i in range(len(lst)):
    elem+=lst[i]
  return elem


def multiply_matrices(mat1,mat2):
  if(not are_multipliable(mat1,mat2)):
    return("Error")
  trans_mat2=mattrans(mat2)
  mat=[[0 for i in range(len(mat2[0]))] for j in range(len(mat1))]
  for i in range(len(mat1)):
    for j in range(len(trans_mat2)):
      lst=multiply_lists(mat1[i],trans_mat2[j])
      mat[i][j]=sum_of_list(lst)
  return(mat)    





if(__name__=="__main__"):
  lst1=input().split(", ")
  lst2=input().split(", ")
  print(add_lists(lst1,lst2))
