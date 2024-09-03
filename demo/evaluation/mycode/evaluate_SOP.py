import functools

sum_of_list = sum

def product_of_list(lst): return functools.reduce(lambda x, y: x * y, lst, 1)

def reduce_terms(e):      return [product_of_list(t) for t in e]

def evaluate_SOP(e):      return sum_of_list(reduce_terms(e))

if __name__ == "__main__": print(evaluate_SOP([[1,2,3], [20, 40]]))
