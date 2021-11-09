def is_wellformed(n):
    k=0
    for i in n:
        if len(i)==len(n[0]):
            k=k+1
    if k==len(n):
        return True
    return False

def are_addable(n,m):
    if is_wellformed(n) and is_wellformed(m) and len(n)==len(m) and len(n[0])==len(m[0]):
        return True
    return False

def are_multipliable(n,m):
    if is_wellformed(n) and is_wellformed(m) and len(n[0])==len(m):
        return True
    return False

def scalar_multiply_list(n,m):
    for i in range(len(m)):
        m[i]=n*m[i]
    return m

def scalar_multiply_matrix(n,m):
    for i in range(len(m)):
        m[i]=scalar_multiply_list(n,m[i])
    return m

def transpose(n):
    n1 = [[n[j][i] for j in range(len(n))] for i in range(len(n[0]))] 
    return n1

def add_lists(n,m):
    k=[0 for x in range(len(n))]
    for i in range(len(n)):
        k[i]=n[i]+m[i]
    return k

def add_matrices(n,m):
    if are_addable(n,m):
        for i in range(len(n)):
            n[i]=add_lists(n[i],m[i])
        return n
    return 'Invlid'

def multiply_lists(n,m):
    k=[0 for x in range(len(n))]
    for i in range(len(n)):
        k[i]=n[i]*m[i]
    return k
    
def sum_list(n):
    k=0
    for i in n:
        k=k+i
    return k

def multiply_matrices(n,m):
    if are_multipliable(n,m):
        g=transpose(m)
        m1=[[0 for x in range(len(m[0]))] for y in range(len(n))]
        for i in range(len(n)):
            for j in range(len(m[0])):
                print(n[i])
                print(g[j])
                m1[i][j]+=sum_list(multiply_lists(n[i],g[j]))
                print(m1[i][j])
        return m1
    return 'Invalid'
