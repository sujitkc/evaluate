def diamond(n,c):
  l=(int)(n/2)

  #For upper triangle
  for i in range(l+1,0,-1):     #For the number of rows
    for j in range(i-1):        #For the blank spaces
      print(" ",end="")
    for k in range(n+(int)(2*(n-1)*(i-1)/(1-n))):     #For the pattern
      print(c,end="")
    print("")

#For lower triangle
  for i in range(1,l+1):        #For the number of rows
    for j in range(i):          #For the blank spaces
      print(" ",end="")
    for k in range(n-2*i):    #For the pattern
      print(c,end="")
    print("")


if(__name__=="__main__"):
  a=int(input())
  b=input()
  char=b[0]
  diamond(a,char)
