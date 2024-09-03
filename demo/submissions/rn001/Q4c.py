def diamond(n,c): 
 if((n%2)!=0):
   p = (n-1)//2
   q = (n+1)//2
   for i in range(q+1): 
     for j in range(p-i+1):
       print(end=" ")
     for k in range((2*i)-1):
       print(c,end="")
     print("\n")
   for i in range(p,0,-1):
     for j in range(q-i):
       print(end=" ")
     for k in range((2*i)-1):
       print(c,end="")
     print("\n") 
 else:
   print("Not possible")

if __name__ =="__main__":   
  n=int(input("type in the number: "))
  c=input("type the character: ")

  diamond(n,c)
      
