def is_wellformed(l):
    for i in range(0,len(l)):
        if(len(l[i-1])!=len(l[i])):
            return False
        else:
            return True
def are_addable(l1,l2):
    if(is_wellformed(l1) and is_wellformed(l2) and len(l1[0])==len(l2[0])):
        return True
    else:
        return False
def are_multipliable(m1,m2):
    if(is_wellformed(m1) and is_wellformed(m2) and len(m2)==len(m1[0])):
        return True
    else:
        return False
def scalar_multiply_list(n,l):
    l1=[]
    for i in range(len (l)):
        l1.append(n*l[i])
    return l1
def scalar_multiply_matrix(n,l):
    l2=[]
    m=[]
    for i in range(len(l)):
        l2.append(m)
        for j in range(len(l[i])):
            l2[i].append(n*l[i][j])
    return l2
def add_lists(l1,l2):
    l=[]
    if(len(l1)==len(l2)):
        for i in range(len(l1)):
            l.append(l1[i]+l2[i])
        return l
def add_matrices(m1,m2):
    lst=[]
    if(are_addable(m1,m2)):
        for i in range(len(m1)):
            lst.append(add_lists(m1[i],m2[i]))
    return lst
def multiply_lists(l1,l2):
    l=[]
    if(len(l1)==len(l2)):
        for i in range(len(l1)):
            l.append(l1[i]*l2[i])
    return l
def transpose(M):
    T=[]    
    for colnum in range(len(M[0])):#to create a zero matrix whose elements will later be replaced to make transpose matrix
        m=[0*i for i in range (len(M))]
        T.append(m)
    #T=[[0,0],[0,0]]
    for rownum in range (len(M)):#for calculating transpose
        for colnum in range (len(M[0])):
            T[colnum][rownum]=M[rownum][colnum]
    return(T)
def sum_of_list(l):
    sum=0
    for i in range(len(l)):
        sum+=l[i]
    return sum
def multiply_matrices(m1,m2):
    m2t=[]
    if(are_multipliable(m1,m2)):
        m2t=transpose(m2)
        m1m2=[]
        l=[]
        w=0
        for i in range(len(m1)):# to get all the elements of the product of m1 and m2 in a single list
            for j in range(len(m2t)):
                product=multiply_lists(m1[i],m2t[j])
                m1m2.append(product)
        for k in range(len(m1)):
            l.append([])#creating empty lists so that product can be expressed as desired
        for a in range(len(m1)):#to create a list l which gives right output
            for b in range(len(m2[0])):
                p=int(sum_of_list(m1m2[w]))
                w=w+1
                l[a].append(p)
        return l
    else:
        return("error")
if __name__=="__main__":
    #print(is_wellformed([[1,2,3],[4,5,6]]))
    #print(is_wellformed([[1,2,3],[20,40]]))
    #print(are_addable([[1,2,3],[20,40,50]],[[1,2,3],[20,40,50]]))
    #print(are_addable([[1,2],[20,40]],[[1,2,3],[20,40,50]]))
    #print(are_multipliable([[1,2,3],[20,40]],[[1,2,3],[20,40,50]]))
    #print(are_multipliable([[1,2],[20,40]],[[1,2,3],[20,40,50]]))
    #print(scalar_multiply_list(3,[1,2,3]))
    #print(scalar_multiply_matrix(3,[[1,2,3]]))
    #print(add_lists([1,2,3],[4,5,6]))
    #print(add_matrices([[1,2,3]],[[4,5,6]]))
    #print(multiply_lists([1,2,3],[4,5,6]))
    #print(sum_of_list([1,2,3]))
    print(multiply_matrices([[1,2,3],[4,5,6]],[[7,10],[8,11],[9,12]]))
    print(multiply_matrices([[3,4,2]],[[13,9,7,15],[8,7,4,6],[6,4,0,3]]))