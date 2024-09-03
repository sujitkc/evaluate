def ndiamond(n):
  p=(n+1)//2
  q=(n-1)//2
  for i in range(p):
    for j in range(q-i):
      print(end=" ")
    for k in range(1,i+2):
      print(k,end="")
    for l in range(i,0,-1):
      print(l,end="")
    print("\n")
  for i in range(q,0,-1):
    for j in range(p-i):
      print(end=" ")
    for k in range(1,i+1):
      print(k,end="")
    for l in range(i-1,0,-1):
      print(l,end="")
    print("\n")

if __name__ == "__main__":
  n=int(input("type in the number: "))

  ndiamond(n)
      
