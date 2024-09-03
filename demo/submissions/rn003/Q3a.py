lst=[]
lst1=[]
def product_of_list(l):
    product=1
    for i in range(len(l)):
        product*=l[i]
    return product
def reduce_terms(l1):
    lst1=[]
    for i in range(len(l1)):
        product=product_of_list(l1[i])
        lst1.append(product)
    return(lst1)
def sum_of_list(l):
    sum=0
    for i in range(len(l)):
        sum+=l[i]
    return sum
def evaluate_SOP(l):
    l1=reduce_terms(l)
    return sum_of_list(l1)
if __name__=="__main__":
    l=[1,2,3]
    print(product_of_list(l))
    print(reduce_terms([[1,2,3],[20,40]]))
    print(sum_of_list([6,800]))
    print(evaluate_SOP([[1,2,3],[20,40]]))
    