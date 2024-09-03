def balanced_brackets(x):
    open = ["(", "[", "{"]
    close = [")", "]", "}"]
    stack = []
    for i in x:
        if i in open:
            stack.append(i)  # appending to stack if it is an opening brace
        elif i in close:
            j = close.index(i)
            if((len(stack) > 0) and (open[j] == stack[len(stack) - 1])):
                stack.pop()  #  removing from stack if corresponding closing brace is present
            else:
                return "False"

    if len(stack) == 0:  # if there is any brace still remaining, then there is no closing brace, hence it is unbalanced
        return "True"
    else:
        return "False"

if __name__ == "__main__":
    x = str(input())
    print(balanced_brackets(x))

