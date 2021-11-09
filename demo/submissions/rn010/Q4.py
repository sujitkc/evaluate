
def is_wellformed(ll):
    for i in range(0, len(ll)-1):
        if (len(ll[i]) != len(ll[i+1])):
            return False
    return True
   
def are_addable(ll1, ll2):
    if is_wellformed(ll1) and is_wellformed(ll2):
        if (len(ll1) == len(ll2)) and (len(ll1[0]) == len(ll2[0])):
            return True
        else:
            return False
    else:
        return False

def are_multipliable(ll1, ll2):
    if is_wellformed(ll1) and is_wellformed(ll2):
        if len(ll1[0]) == len(ll2):
            return True
        else:
            return False
    else:
        return False

def scalar_multiply_list(n, l):
    return [n*i for i in l]

def scalar_multiply_matrix(n, ll):
    return [scalar_multiply_list(n, l) for l in ll]

def add_lists(l1, l2):
    return [l1[i]+l2[i] for i in range(len(l1))]

def add_matrices(ll1, ll2):
    if are_addable(ll1, ll2):
        return [add_lists(ll1[i], ll2[i]) for i in range(len(ll1))]
    else:
        return "Non-addable"

def multiply_lists(l1, l2):
    return [l1[i]*l2[i] for i in range(len(l1))]

def transpose(l):
        n = len(l)
        m = len(l[0])
        lret = [[] for i in range(m)]
        for i in range(m):
            for j in range(n):
                lret[i].append(l[j][i])
        return lret

def sum_of_list(l):
    sum1 = 0
    for i in l:
        sum1 += i
    return sum1

def multiply_matrices(ll1, ll2):
    if are_multipliable(ll1, ll2):
        llret = [[] for i in ll1]
        ll2 = transpose(ll2)
        for i in range(len(ll1)):
                for j in range(len(ll2)):
                    llret[i].append(sum_of_list(multiply_lists(ll1[i], ll2[j])))
        return llret
    else:
        return "Can not be multiplied"
