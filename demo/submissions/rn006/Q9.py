def even_elements(l):
  l=[(int)(x) for x in l]
  return [x for x in l if x%2==0]

if(__name__=="__main__"):
  l=input().split(", ")
  lst=even_elements(l)
  print(lst)
