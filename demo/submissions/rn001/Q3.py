def product_of_list(mat):
  k=1
  for el in mat:
    k=k*el
  return k
  
def reduce_terms(mat):
  lans=[]
  for a in range(len(mat)):
    k=product_of_list(mat[a])
    lans.append(k)  
  
  return(lans)
  
def sum_of_list(mat):
  k=0
  for el in mat:
    k=k+el
  return k
  
def evaluate_SOP(mat):
  lans=[]
  for a in range(len(mat)):
    k=1
    for el in mat[a]:
      k=k*el
    lans.append(k)
  p=0
  for el in lans:
    p=p+el
  return p
  
  
if __name__ == "__main__":
 
  print ( product_of_list ([1 , 2 , 3]))
  print ( reduce_terms ([[1 , 2 , 3] , [20 , 40]]))
  print ( sum_of_list ([6 , 800]))
  print ( evaluate_SOP ([[1 , 2 , 3] , [20 , 40]]))
