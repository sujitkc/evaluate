def product_of_list(n):
    k=1
    for i in n:
        k=k*i
    return k

def reduce_terms(n):
    for i in range(len(n)):
        n[i]=product_of_list(n[i])
    return n

def sum_of_list(n):
    k=0
    for i in n:
        k=k+i
    return k

def evaluate_SOP(n):
    n=reduce_terms(n)
    n=sum_of_list(n)
    return n
