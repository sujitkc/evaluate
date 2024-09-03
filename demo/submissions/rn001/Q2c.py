def print_n_messages(msg):
  for i in range(10):
    print(msg)

if __name__ =="__main__":      
  msg = input("type in any message to be printed 10 times: ")

  print_n_messages(msg)
