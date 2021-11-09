
#DISCLAIMER
#there are many if name==main statements as I did not realize in the start that all of them had to be part 
# of same file instead of a,b,c... Thus I copy pasted them and this the result.I hope it is not a problem


def is_wellformed(m1):

    l1=len(m1[0])

    for i in m1:
        if len(i)!=l1:
            return False

    else:
        return True



if __name__ == "__main__":
    print ( is_wellformed ([[1 , 2 , 3] , [20 , 40 , 50]]))
    print ( is_wellformed ([[1 , 2 , 3] , [20 , 40]]))



def are_addable(m1,m2):

    if (is_wellformed(m1) and is_wellformed(m2)) and len(m1)==len(m2) and len(m1[0])==len(m2[0]):

        return True

    return False



if __name__ == "__main__":
    print ( are_addable ([[1 , 2 , 3] , [20 , 40 , 50]] , [[1 , 2 , 3] , [20 , 40 , 50]]))
    print ( are_addable ([[1 , 2] , [20 , 40]] , [[1 , 2 , 3] , [20 , 40 , 50]]))


def are_multipliable(m1,m2):

    if is_wellformed(m1) and is_wellformed(m2) and len(m1[0])==len(m2) :

        return True


    return False


if __name__ == "__main__":
    print( are_multipliable([[1 , 2 , 3] , [20 , 40 , 50]] , [[1 , 2 , 3] , [20 , 40 , 50]]))
    print ( are_multipliable([[1 , 2] , [20 , 40]] , [[1 , 2 , 3] , [20 , 40 , 50]]))


def scalar_multiply_list(k,l):

    n=[i*k for i in l]

    return n

if __name__ == "__main__":
    print(scalar_multiply_list(3,[1,2,3]))

def scalar_multiply_matrix(k,m):

    n=[scalar_multiply_list(k,i) for i in m]

    return n


if __name__ == "__main__":
    print ( scalar_multiply_matrix (3 , [[1 , 2 , 3]]))




def add_lists(l1,l2):

    l=[l1[i]+l2[i] for i in range(len(l1))]

    return l


if __name__ == "__main__":
    print ( add_lists ([1 , 2 , 3] , [4 , 5 , 6]))


def add_matrices(m1,m2):

    if not are_addable(m1,m2):
        return "Cannot be added"

    l=[add_lists(m1[i],m2[i]) for i in range(len(m1))]


    return l


if __name__ == "__main__":
    print ( add_matrices ([[1 , 2 , 3]] , [[4 , 5 , 6]]))
    print ( add_matrices ([[1 , 2 , 3],[1,2,4]] , [[4 , 5 , 6]]))



def multiply_lists(l1,l2):


    l=[l1[i]*l2[i] for i in range(len(l1))]

    return l

if __name__ == "__main__":
    print ( multiply_lists ([1 , 2 , 3] , [4 , 5 , 6]))


def mattrans(l):

        n=[]

        for i in range(len(l[0])):

                m=[]

                for j in range(len(l)):

                        m.append(l[j][i])

                n.append(m)

        return n


def multiply_matrices(m1,m2):

    if not are_multipliable(m1,m2):

        return "not multipliable"


    m2t=mattrans(m2)#transpose of m2
    print("transpose of m2 is ",m2t)

    l=[]

    for i in range(len(m1)):

        n=[sum(multiply_lists(m1[i],m2t[j]))  for j in range(len(m2t))]
        l.append(n)

    return l


if __name__ == "__main__":
    print ( multiply_matrices ([[1 , 2 , 3] ,[4 , 5 , 6]] ,
[[7 , 10] , [8 , 11] , [9 , 12]]))
