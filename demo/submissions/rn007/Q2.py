def increment(n):
  x=n+1
  return x

def decrement(n):
  x=n-1
  return x

def add(x,y):
  a=increment(x)+increment(y)-2
  return a

def subtract(x,y):
  s=decrement(x)-decrement(y)
  return s

def multiply(x,y):
  m=0
  for i in range(y):
    m=add(x,m)
  return m

def divide(x,y):
  m=x
  for i in range(y):
    m=subtract(m,y) 
  return m

def exponent(x,y):
  e=1
  for i in range(y):
    e=e*multiply(x,1)
  return e

if __name__=="__main__":
  print(increment(1))
  print(decrement(1))
  print(add(1,2))
  print(subtract(1,2))
  print(multiply(5,6))
  print(divide(7,2))
  print(exponent(2,3))
