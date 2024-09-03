def ndiamond():
  #For upper triangle
  for i in range(3,0,-1):       #For the number of rows
    for j in range(i-1):        #For the blank spaces
      print(" ",end="")
    for k in range(4-i):        #For left upper half
      print(k+1,end="")
    for l in range(3-i,0,-1):   #For right upper half
      print(l,end="")
    print("")


  #For lower triangle
  for i in range(1,3):          #For the number of rows
    for j in range(i):          #For the blank spaces
      print(" ",end="")
    for k in range(3-i):        #For left lower half
      print(k+1,end="")
    for l in range(2-i,0,-1):   #For right lower half
      print(l,end="")
    print("")


if(__name__=="__main__"):
  ndiamond()
