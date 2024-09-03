def even_elements(l):
  for el in l:
    if(el%2==0):
      le.append(el)
  print(le)  

l = []
le = []

if __name__ == "__main__":
  n = int(input("type in a limit for the number of elements: "))

  for i in range(n):
    x = int(input("type in the element: "))  # makes a list from 1 to n
    l.append(x)

  even_elements(l)

