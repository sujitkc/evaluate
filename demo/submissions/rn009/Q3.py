def product_of_list(lst):
    x=1
    for i in lst:
        x*=i
    return x
def reduce_terms(lst):
    lst1=[]
    for i in lst:
        lst1.append(product_of_list(i))
    return lst1
def sum_of_list(lst):
    x=0
    for i in lst:
        x+=i
    return x
def evaluate_SOP(lst):
    lst=reduce_terms(lst)
    sop=sum_of_list(lst)
    return sop

if __name__ =="__main__":
    print(product_of_list([1,2,3]), reduce_terms([[1, 2, 3], [20,  40]]), sum_of_list([800,6]), evaluate_SOP([[1, 2, 3], [20,  40]]))
