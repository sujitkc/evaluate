def diamond():
  #For upper triangle
  for i in range(3,0,-1):      #For the number of rows
    for j in range(i-1):       #For the blank spaces
      print(" ",end="")
    for k in range(7-2*i):     #For the pattern
      print("*",end="")
    print("")

  #For lower triangle
  for i in range(1,3):        #For the number of rows
    for j in range(i):        #For the blank spaces
      print(" ",end="")
    for k in range(5-2*i):    #For the pattern
      print("*",end="")
    print("")

if(__name__=="__main__"):
  diamond()
