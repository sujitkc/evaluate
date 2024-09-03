def ndiamond():
  for i in range(1,4):
    for j in range(3-i):
      print(end=" ")
    for k in range(1,i+1):
      print(k,end="")
    for x in range(i-1,0,-1):
      print(x,end="")
    print("\n")
  for i in range(2,0,-1):
    for j in range(3-i):
      print(end=" ")
    for k in range(1,i+1):
      print(k,end="")
    for x in range(i-1,0,-1):
      print(x,end="")
    print("\n")

if __name__ == "__main__":
  ndiamond()
      
