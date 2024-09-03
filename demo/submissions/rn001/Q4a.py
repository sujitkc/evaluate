def diamond(): 
  for i in range(1,4): 
    for j in range(1,4-i):
      print(end=" ")
    for k in range((2*i)-1):
      print("*",end="")
    print("\n")
  for i in range(2,0,-1):
    for j in range(3-i):
      print(end=" ")
    for k in range((2*i)-1):
      print("*",end="")
    print("\n")

 
if __name__ =="__main__":  
  diamond() 

