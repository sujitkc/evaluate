def diamond(n,c):
  for i in range(1,n,2):
    print(" "*(n//2-i//2),c*i)
  for i in range(n,0,-2):
    print(" "*(n//2-i//2),c*i)

if __name__=="__main__":
  n=int(input())
  c=input()
  diamond(n,c)