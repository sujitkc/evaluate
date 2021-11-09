def is_wellformed(mat):   #a
    check=0
    for i in range(len(mat)-1):
        if(len(mat[i])!=len(mat[i+1])):
            check=1
            break
    if(check==0):
        return True
    else:
        return False

def are_addable(lst1,lst2):   #b
    if (is_wellformed(lst1)==True and is_wellformed(lst2)==True):
        if(len(lst1)==len(lst2) and len(lst1[0])==len(lst2[0])):
            return True
        else:
            return False
    else:
        return False

def are_multipliable(mat1,mat2):    #c
    if (is_wellformed(mat1)==True and is_wellformed(mat2)==True):
        if(len(mat1[0])==len(mat2)):
            return True
        else:
            return False
    else:
        return False

def scalar_multiply_list(n,lst):   #d
    for i in range(len(lst)):
        lst[i]=int(lst[i])*n
    return lst

def scalar_multiply_matrix(n,mat):   #e
    for i in range(len(mat)):
        mat[i] = scalar_multiply_list(n,mat[i])
    return mat

def add_lists(lst1,lst2):   #f
    lst=[]
    if (len(lst1)==len(lst2)):
        for i in range(len(lst1)):
            lst.append(lst1[i]+lst2[i])
        return lst
    else:
        return "Error"

def add_matrices(mat1,mat2):   #g
    mat=[]
    if (are_addable(mat1,mat2)==True):
        for i in range(len(mat1)):
            mat.append(add_lists(mat1[i],mat2[i]))
        return mat
    else:
        return "Error"

def multiply_lists(lst1,lst2):   #h
    lst=[]
    if (len(lst1)==len(lst2)):
        for i in range(len(lst1)):
            lst.append(int(lst1[i])*int(lst2[i]))
        return lst
    else:
        return "Error"

def transpose(m):
    mat=[]
    r = len(m)
    c = len(m[0])
    for i in range(c):
        inter=[]
        for j in range(r):
            inter.append(m[j][i])
        mat.append(inter)
    return mat

def sum_of_list(lst):
    x=0
    for i in lst:
        x+=i
    return x

def multiply_matrices(mat1,mat2):  #i
    mat=[]
    if(are_multipliable(mat1,mat2)==True):
        mat2=transpose(mat2)
        for i in range(len(mat1)):
            r=[]
            for j in range(len(mat1)):
                r.append(sum_of_list(multiply_lists(mat1[i],mat2[j])))
            mat.append(r)
        return mat

if __name__ == "__main__":
    print(is_wellformed([[1, 2, 3], [20, 40, 50]]),is_wellformed ([[1, 2, 3], [20,  40]]))
    print(are_addable([[1, 2, 3], [20, 40, 50]], [[1, 2, 3], [20, 40, 50]]))
    print(are_addable([[1, 2], [20, 40]], [[1, 2, 3], [20, 40, 50]]))
    print(are_multipliable([[1, 2, 3], [20, 40, 50]], [[1, 2, 3], [20, 40, 50]]))
    print(are_multipliable([[1, 2], [20, 40]], [[1, 2, 3], [20, 40, 50]]))
    print(scalar_multiply_list(3, [1, 2, 3]))
    print(scalar_multiply_matrix(3, [[1, 2, 3]]))
    print(add_lists([1, 2, 3], [4, 5, 6]))
    print(add_matrices([[1, 2, 3]], [[4, 5, 6]]))
    print(multiply_lists([1, 2, 3], [4, 5, 6]))
    print(transpose([[4, 6, 9], [1, 2, 3]]))
    print(multiply_matrices([[1, 2, 3], [4, 5, 6]],[[7, 10], [8,11], [9,12]]))