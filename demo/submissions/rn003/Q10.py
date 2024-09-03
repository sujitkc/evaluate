def balanced_brackets(n):
    stack=[]
    for i in range (len(n)):
        if '('==n[i] or'{'==n[i] or '['==n[i]: 
            stack.append(n[i])
        elif (')'==n[i] or '}'==n[i] or ']'==n[i]):
            if (len(stack)==0) or (stack[-1]+n[i] not in {'()','{}','[]'}):
                return False
            else:
                stack.pop()
    return len(stack)==0
if __name__=="__main__":
    n=[x for x in str(input())]
    print(balanced_brackets(n))
