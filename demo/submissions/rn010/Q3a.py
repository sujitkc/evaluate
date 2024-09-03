
def product_of_list(l):
    product = 1
    for i in l:
        product *= i
    return product

def reduce_terms(ll):
    redlist = []
    for l in ll:
        redlist.append(product_of_list(l))
    return redlist

def sum_of_list(l):
    sum1 = 0
    for i in l:
        sum1 += i
    return sum1

def evaluate_SOP(ll):
    l = reduce_terms(ll)
    return sum_of_list(l)

