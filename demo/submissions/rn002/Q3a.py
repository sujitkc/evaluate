# Solution for 3rd question

#3(a)
def product_of_list(l):
    result=1
    for ele in l:
        result=result*ele
    return (result)

#3(b)
def reduce_terms(e):
    new_list=[product_of_list(sub_e) for sub_e in e]
    return(new_list)

#3(b)
def sum_of_list(l):
    result=0
    for ele in l:
        result+=ele
    return(result)

#3(d)
def evaluate_SOP(l):
    l= reduce_terms(l)
    l=sum_of_list(l)
    return(l)

if __name__=="__main__":
    print(product_of_list([1,2,3]))
    print(reduce_terms([[1,2,3],[20,40]]))
    print(sum_of_list([6,800]))
    print(evaluate_SOP([[1,2,3],[20,40]]))
