
def matmul(m1, m2):
    m1m = len(m1)
    m1n = len(m1[0])
    m2m = len(m2)
    m2n = len(m2[0])
    if (m1n == m2m):    
        mres = [[] for i in range(m1m)]
        for k in range(m1m):
            for i in range(m2n):
                temp = 0
                for j in range(m2m):
                    temp += m1[k][j]*m2[j][i]
                mres[k].append(temp)
        return mres
    else:
        return "Matrices cannot be multiplied :("

