#DISCLAIMER
#there are many if name==main statements as I did not realize in the start that all of them had to be part 
# of same file instead of a,b,c... Thus I copy pasted them and this the result.I hope it is not a problem



def product_of_list(l):

    p=1
    for i in l:
        p*=i

    return p


if __name__ == "__main__":
    print(product_of_list([1,2,3]))

def reduce_terms(n):

    l=[product_of_list(i) for i in n]

    return l


if __name__ == "__main__":
    print(reduce_terms([[1,2,3],[4,5,6]]))


def sum_of_list(l):

    return sum(l)


if __name__ == "__main__":
    print(sum_of_list([1,2,3,4]))


def evaluate_SOP(l):

    n=reduce_terms(l)
    
    m=sum_of_list(n)

    return m


if __name__ == "__main__":
    print(evaluate_SOP([[1,2,3],[20,40]]))
