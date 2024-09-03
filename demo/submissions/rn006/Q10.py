def balanced_brackets(string):
  stack=[]
  for i in range(len(string)):
    if(string[i]=='(' or string[i]=='{' or string[i]=='['):
      stack.append(string[i])
    elif(string[i]==')' or string[i]=='}' or string[i]==']'):
      if(stack==[]):
        return("False")
      elif((stack[len(stack)-1] =='(' and string[i]==')') or (stack[len(stack)-1] =='{' and string[i]=='}') or (stack[len(stack)-1] =='[' and string[i]==']')):
        stack.pop()
      else:
        return("False")

  return("True" if stack==[] else "False")

if(__name__=="__main__"):
  string=input("Enter the string: ")
  print(balanced_brackets(string))
