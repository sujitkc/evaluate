def print_n_messages(msg,n):
   for i in range(n):
     print(msg)

if __name__ =="__main__":       
  n = int(input("give an input for the number of times the message has to be printed(n): "))
  msg = input("type in a message to be printed(msg): ")

  print_n_messages(msg,n)
