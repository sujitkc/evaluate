# Solution for problem 4th

#(a)
def is_wellformed(m):
    k = 1
    for i in range(len(m)):
        for j in range(len(m)):
            if(len(m[i])!=len(m[j])):
                k=0
    if (k==1):
        return True
    if(k==0):
        return False
#(b)
    
def are_addable(a,b):
    if(len(a)==len(b) and len(a[0])==len(b[0])):
        return True
    else:
        return False
#(c)
def are_multipliable(m1,m2):
    a=is_wellformed(m1)
    b=is_wellformed(m2)

    if(a and b):
        if(len(m1[0])==len(m2)):
            return True
        else:
            return False
    else:
        return False

#(d)
    
def scalar_multiply_list(n,l):
    l_res = [ n*l[i] for i in range(len(l))]
    return(l_res)

#(e)

def scalar_multiply_matrix(n,m):
    if is_wellformed(m) == True:
        m_res = [ scalar_multiply_list(n,m[i]) for i in range(len(m)) ]
        return(m_res)

def are_multipliable(m1,m2):
    if ( is_wellformed(m2) == True and is_wellformed(m1) == True and len(m1[0]) == len(m2) ):
        return True
    return False            

def scalar_multiply_list(n,l):
    result = [ n*l[i] for i in range(len(l))]
    return(result)    

def scalar_multiply_matrix(n,m):
    if is_wellformed(m) == True:
        result = [ scalar_multiply_list(n,m[i]) for i in range(len(m)) ]
        return(result)

#(f)

def add_lists(l1,l2):
    if len(l1) == len(l2):
        l = [ (l1[i] + l2[i]) for i in range(len(l1)) ]
        return(l)

#(g)

def add_matrices(m1,m2):
    if are_addable(m1,m2) == False:
        print("the matrices given in input are not addable")
    else:
        M = [ add_lists(m1[i],m2[i]) for i in range(len(m1)) ]
        return(M)

#(h)

def multiply_lists(l1,l2):
    if len(l1) == len(l2):
        l = [ l1[i] * l2[i] for i in range(len(l1)) ]
        return(l)

#(i)

def multiply_matrices(m1,m2):
    if are_multipliable(m1,m2) == False:
        print("the matrices given in input are not multipliable")
    else:
        m2t = transpose(m2)
        multiply_matrix = [[ sum_of_list(multiply_lists(m1[i],m2t[j])) for j in range(len(m2t)) ]for i in range(len(m1)) ]
        return(multiply_matrix)
 
 
def transpose(m):
    if is_wellformed(m) == True:
        s = 0
        M = [ [(m[i][j]) for i in range(len(m)) ] for j in range(len(m[0])) ]
        return(M)
 
 
def sum_of_list(l):
    s = 0
    for i in range(len(l)):
        s += l[i]
    return(s)        
            
if __name__ == '__main__':

    print ( is_wellformed ([[1 , 2 , 3] , [20 , 40 , 50]]))
    print ( is_wellformed ([[1 , 2 , 3] , [20 , 40]]))
    print ( are_addable ([[1 , 2 , 3] , [20 , 40 , 50]] , [[1 , 2 , 3] , [20 , 40 , 50]]))
    print ( are_addable ([[1 , 2] , [20 , 40]] , [[1 , 2 , 3] , [20 , 40 , 50]]))
    print ( are_multipliable ([[1 , 2 , 3] , [20 , 40 , 50]] , [[1 , 2 , 3] , [20 , 40 , 50]]))
    print ( are_multipliable ([[1 , 2] , [20 , 40]] , [[1 , 2 , 3] , [20 , 40 , 50]]))
    print ( scalar_multiply_list (3 , [1 , 2 , 3]))
    print ( scalar_multiply_matrix (3 , [[1 , 2 , 3]]))
    print ( add_lists ([1 , 2 , 3] , [4 , 5 , 6]))
    print ( add_matrices ([[1 , 2 , 3]] , [[4 , 5 , 6]]))
    print ( multiply_lists ([1 , 2 , 3] , [4 , 5 , 6]))
    print ( multiply_matrices ([[1 , 2 , 3] ,[4 , 5 , 6]] ,[[7 , 10] , [8 , 11] , [9 , 12]]))

 








































        
