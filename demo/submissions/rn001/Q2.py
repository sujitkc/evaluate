def increment(a):
  return a+1
  
def decrement(a):
  return a-1
  
def add(a,b):
  k=a
  for i in range(b):
    k=increment(k)
  return k

def subtract(a,b):
  k=a
  for i in range(b):
    k=decrement(k)
  return k
  
def multiply(a,b):
  k=0
  for i in range(b):
    k=k+a
  return(k)

def divide(a,b):
  k=a
  count=1
  while((k-b)!=0):
    count += 1
    k=k-b
  return(count)
  
def exponent(a,b):
  
  k=a
  p=a
  for i in range(b-1):
    k=multiply(k,p)
  return(k)
  
if __name__ == "__main__":
  
  a =int(input("type in the input: "))
  b =int(input("type in the input: "))
  print (increment (a))
  print (decrement(a))
  print (add(a,b))
  print (subtract(a,b))
  print (multiply(a,b))
  print (divide(a,b))
  print(exponent(a,b))
  
