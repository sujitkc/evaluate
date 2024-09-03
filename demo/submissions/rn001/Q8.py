def double(l):
  for el in l:
    new=2*el
    lD.append(new)
  print(lD)

l = []
lD = []

if __name__ == "__main__":
  n = int(input("type in the element limit for the list: "))

  for i in range(1,n+1): # makes a list from 1 to n
    x = int(input("type in the elements: ")) 
    l.append(x)
  
  double(l)

