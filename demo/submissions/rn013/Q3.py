def product_of_list(x):
    z = 1
    for i in x:
        z = z*i
    return z

def reduce_terms(e):
    l = [product_of_list(i) for i in e]
    return l

def sum_of_list(x):
    z = 0
    for i in x:
        z = z + i
    return z

def evaluate_SOP(e):
    l = (reduce_terms(e))
    return sum_of_list(l)

if __name__ == "__main__":
    print(product_of_list([1, 2, 3]))
    print(reduce_terms([[1, 2, 3], [20, 40]]))
    print(sum_of_list([6, 800]))
    print(evaluate_SOP([[1, 2, 3], [20, 40]]))









