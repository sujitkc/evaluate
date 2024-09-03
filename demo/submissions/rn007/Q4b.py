def diamond(n):
  for i in range(1,n,2):
    print(" "*(n//2-i//2),"*"*i)
  for i in range(n,0,-2):
    print(" "*(n//2-i//2),"*"*i)

if __name__=="__main__":
  n=int(input())
  diamond(n)