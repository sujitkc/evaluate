def balanced_brackets(s):
    a=0
    b=0
    c=0
    for i in s:
        if i=='(':
            a+=1
        elif i==')':
            a-=1
            if a<0:
                return 'False'
        elif i=='{':
            b+=1
        elif i=='}':
            b-=1
            if b<0:
                return 'False'
        elif i=='[':
            c+=1
        elif i==']':
            c-=1
            if c<0:
                return 'False'
    if a==0 and b==0 and c==0:
        return 'True'
    return 'False'
