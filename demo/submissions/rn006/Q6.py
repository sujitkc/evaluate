def ndiamond(n):

  #For upper triangle
  for i in range((int)(n/2)+1,0,-1):           #For the number of rows
    for j in range(i-1):                     #For the blank spaces
      print(" ",end="")
    for k in range((int)((n+3)/2)-i):         #For left upper half
      print(k+1,end="")
    for l in range((int)((n+1)/2)-i,0,-1):   #For right upper half
      print(l,end="")
    print("")


  #For lower triangle
  for i in range(1,(int)(n/2)+1):              #For the number of rows
    for j in range(i):                       #For the blank spaces
      print(" ",end="")
    for k in range((int)((n+1)/2)-i):        #For left lower half                                                   
      print(k+1,end="")
    for l in range((int)((n-1)/2)-i,0,-1):   #For right lower half
      print(l,end="")
    print("")


if(__name__=="__main__"):
  n=int(input())
  ndiamond(n)
