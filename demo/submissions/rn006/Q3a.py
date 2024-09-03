def product_of_list(lst):
  prod=1
  for i in range(len(lst)):
    prod=prod*(int)(lst[i])
  return(prod)


def sum_of_list(lst):
  add=0
  for i in range(len(lst)):
    add=add+lst[i]
  return add


def reduce_terms(lst):
  a=[]  
  for i in range(len(lst)):
    a.append(product_of_list(lst[i]))
  return(sum_of_list(a))


def evaluate_SOP(lst):
  return(reduce_terms(lst))



if(__name__=="__main__"):
  lst1=[]
  for i in range(2): 
    lst=input().split(", ")
    lst1.append(lst)
  print(evaluate_SOP(lst1))
