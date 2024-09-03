def banner(msg):
  for i in range(20):
    print("*",end="")
  print("\n")
  print("* "+msg+" *")
  print("\n")
  for i in range(20):
    print("*",end="")

if __name__ =="__main__":      
  msg = input("type in a text to be printed: ")

  banner(msg)  
