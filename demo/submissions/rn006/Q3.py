def banner(m):
  b=len(m)
  for i in range(b+4):
    print("*",end="")
  print("")
  print("* "+m+" *")
  for i in range(b+4):
    print("*",end="")
  print("")

if(__name__=="__main__"):
  n=input()
  banner(n)
