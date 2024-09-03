def double(l):
  l=[(int)(x) for x in l]
  return [2*x for x in l]

if(__name__=="__main__"):
  l=input().split(", ")
  lst=double(l)
  print(lst)
