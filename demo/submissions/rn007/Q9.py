def even_elements(l):
  result=[]
  for i in range(len(l)):
    if l[i]%2==0:
      result.append(l[i])
  return result

if __name__=="__main__":
  n=int(input())
  lst = []
  for i in range(1,n+1):
    a=int(input())
    lst.append(a)
  result=even_elements(lst)
  print(result)


