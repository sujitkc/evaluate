def is_wellformed(x):
    k = len(x[0])
    flag = 0
    i = 0
    for i in range (0, len(x)):
        if (len(x[i]) == k):    # comparing length of all rows to the first row
            flag = 0
        else:
            flag = 1
    if (flag == 0):
        return("True")
    else:
        return("False")

def are_addable(x, y):
    if ((is_wellformed(x) == "True") & (is_wellformed(y) == "True") & (len(x) == len(y)) & (len(x[0]) == len(y[0]))):
        return "True"
    else:
        return "False"

def are_multipliable(m1, m2):
    if((is_wellformed(m1) == "True") & (len(m1[0]) == len(m2))):
        return ("True")
    else:
        return ("False")


def scalar_multiply_list(x, y):
    l = [x*i for i in y]
    return l

def scalar_multiply_matrix(x, y):
    l = []
    for i in y:
        l.append(scalar_multiply_list(x, i))
    return l

def add_lists(l1, l2):

    l = []
    for i in range(0, len(l1)):
        l.append(l1[i] + l2[i])
    return l


def add_matrices(m1, m2):
    if(are_addable(m1, m2) == "True"):
        l = []
        for i in range(0, len(m1)):
            l.append(add_lists(m1[i], m2[i]))
        return l
    else:
        print("Cannot be added")
        exit()

def multiply_lists(l1, l2):
    l = []
    for i in range(0, len(l1)):
        l.append(l1[i]*l2[i])
    return l

def transpose(x):
    l1 = []
    l = []
    for i in range(0, len(x[0])):
        l = []
        for j in range(0, len(x)):
            l.append(x[j][i])
        l1.append(l)
    return l1

def sum_of_list(x):
    z = 0
    for i in range(0, len(x)):
        z = z + x[i]
    return z

def multiply_matrices(m1, m2):
    if(are_multipliable(m1, m2) == "True"):
        m2t = transpose(m2)
        l1 = []
        for i in range(0, len(m1)):
            l = []
            for j in range(0, len(m2t)):
                l.append(sum_of_list(multiply_lists(m1[i], m2t[j])))
            l1.append(l)
        return l1

    else:
        print("Cannot be multiplied")
        exit()


if __name__ == "__main__":
    print(is_wellformed([[1, 2, 3], [20, 40, 50]]))
    print(are_addable([[1, 2], [20, 40]], [[1, 2, 3], [20, 40, 50]]))
    print(are_multipliable([[1, 2], [20, 40]], [[1, 2, 3], [20, 40, 50]]))
    print(scalar_multiply_list(3, [1, 2, 3]))
    print(scalar_multiply_matrix(3, [[1, 2, 3], [4, 5, 6]]))
    print(add_lists([1, 2, 3], [4, 5, 6]))
    print(add_matrices([[1, 2, 3], [4, 5, 6], [7, 8, 9]], [[2, 4, 6], [3, 4, 5], [1, 2, 3]]))
    print(multiply_lists([1, 2, 3], [4, 5, 6]))
    print(transpose([[1, 2, 3], [4, 5, 6], [7, 8, 9], [10, 11, 12]]))
    print(multiply_matrices([[1, 2, 3], [4, 5, 6]], [[7, 10], [8, 11], [9, 12]]))

