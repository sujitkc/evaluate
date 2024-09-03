
def balanced_brackets(seq):
    stack=[]
    for char in seq:                     #checking for every parenthesis
        if char in ['{','[','(']:        #if it is opening parenthesis then add it in stack 
            stack.append(char)

        if char in ['}',']',')']:
                                         #if closing bracket is encountered then in ideal case stack should not be empty
            if not stack:
                return False

            top_char = stack.pop()       #last element of stack 
                                         #all ifs returns false when matching pair of parenthesis is not encountered
            if top_char=='(':   
                if char != ')':
                    return False
            if top_char=='{':
                if char != '}':
                    return False
            if top_char=='[':
                if char != ']':
                    return False       #after every char in seq is either removed or added;
                                       #we now have to see if stack is empty or not
                                       #if stack is empty then the expression is balanced

    if stack:
        return False
    else:
        return True

if __name__=="__main__":
    print(balanced_brackets(input()))
