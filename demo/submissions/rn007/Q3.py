def product_of_list(lst):
  p=1
  for i in range(len(lst)):
    p=p*lst[i]
  return p

def reduce_terms(lst):
  k=[]
  for i in range(len(lst)):
    p=product_of_list(lst[i])
    k.append(p)
  return k

def sum_of_list(lst):
  sum=0
  for i in range(len(lst)):
    sum=sum+lst[i]
  return sum

def evaluate_SOP(lst):
  a=reduce_terms(lst)
  sop=sum_of_list(a)
  return sop

if __name__=="__main__":
  print(product_of_list([1,2,3]))
  print(reduce_terms([[1,2,3],[20,40]]))
  print(sum_of_list([6,800]))
  print(evaluate_SOP([[1,2,3],[20,40]]))
