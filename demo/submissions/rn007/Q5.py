def ndiamond():
  p=int(5/2)+1
  z=1
  q=p-1
  lst=[]
  for i in range(p):
    k=""
    print(" "*q,end="")
    k=" "*q
    for j in range(1,z+1):
      print(j,end="")
      k=k+str(j)
    m=z-1
    for j in range(m,0,-1):
      print(j,end="")
      k=k+str(j)
    q=q-1
    z=z+1
    lst.append(k)
    print()
  for i in range(len(lst)-2,-1,-1):
    print(lst[i])
       
if __name__=="__main__":
  ndiamond()