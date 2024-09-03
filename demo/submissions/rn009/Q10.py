def balanced_brackets(str):
    stack=[]
    for i in str:
        if (i=="(" or i=="{" or i=="["):
            stack.append(i)
        elif (i==")" or i=="}" or i=="]"):
            if (len(stack)==0):
                return False
            if ((i==")" and stack[-1]=="(") or (i=="}" and stack[-1]=="{") or (i=="]" and stack[-1]=="[")):
                stack.pop()
            else:
                return False
    if (len(stack)==0):
        return True
    else:
        return False


if __name__ == "__main__":
    s = input()
    out = balanced_brackets(s)
    print(out) 
