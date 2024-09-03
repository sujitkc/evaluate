
def mattrans(l):
    n = len(l)
    m = len(l[0])
    lret = [[] for i in range(m)]
    for i in range(m):
        for j in range(n):
            lret[i].append(l[j][i])
    return lret

