def double(l):
  result =[]
  for i in range(len(l)):
    r=2*l[i]
    result.append(r)
  return result
if __name__=="__main__":
  n = int(input())
  lst=[]
  for i in range(1,n+1):
    a=int(input())
    lst.append(a)
  result=double(lst)
  print(result)


