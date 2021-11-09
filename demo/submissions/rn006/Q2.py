def increment(a):
  return a+1

def decrement (a):
  return a-1

def add(a,b):
  for i in range(b):
    a=increment(a)
  return a

def subtract(a,b):
  for i in range(b):
    a=decrement(a)
  return a

def multiply(a,b):
  n=a
  for i in range(b-1):
    a=add(a,n)
  return a

def divide(a,b):
  n=0
  while(1):
    if(a<b):
      break
    else:
      n=n+1
      a=subtract(a,b)
  return n

def exponent(a,b):
  n=a
  for i in range(b-1):
    a=multiply(a,n)
  return a



if(__name__=="__main__"):
  a=int(input("a="))
  b=int(input("b="))
  print("Increment ",increment(a))
  print("Decrement ",decrement(a))
  print("Addition ",add(a,b))
  print("Subtraction ",subtract(a,b))
  print("Multiplication ",multiply(a,b))
  print("Division ",divide(a,b))
  print("Exponent ",exponent(a,b))

