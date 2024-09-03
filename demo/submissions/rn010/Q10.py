
def balanced_brackets(l):
    l = [i for i in l]
    l2 = []
    for i in l:
        if ((i == "{") or  (i == "[") or (i =="(")):
            l2.append(i)
        elif i == "}":
            if l2 == []:
                return False
            if l2[-1] == "{":
                l2.pop()
        elif i == "]":
            if l2 == []:
                return False
            if l2[-1] == "[":
                l2.pop()
        elif i == ")":
            if l2 == []:
                return False
            if l2[-1] == "(":
                l2.pop()
    if l2 == []:
        return True
    else:
        return False

