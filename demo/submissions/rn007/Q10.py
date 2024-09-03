def balanced_brackets(l):
  st1 = []
  for char in l:
    st1.append(char)
  k=len(st1)
  for i in range(len(st1)):
    j=len(st1)-i-1
    if(st1[i] != st1[j]):
      k=i
      break
  if(k==len(st1)):
    return True
  else:
    return False

if __name__=="__main__":
  lst = input()
  print(balanced_brackets(lst))
