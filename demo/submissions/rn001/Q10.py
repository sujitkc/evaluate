def balanced_brackets(char):
  ope=['[','(','{']
  clo={']':'[','}':'{',')':'('}
  stack=[]
  for i in char:
    if i in ope:
      stack.append(i)
    elif i in clo: 
      p =clo[i]
      if (len(stack)!=0 and p==stack[-1]):
        stack.pop()     
  if len(stack)==0:
    print("True")      
  else :
    print("False")

if __name__ == "__main__":
  char = input("type in the input: ")

  balanced_brackets(char)
