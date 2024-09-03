def matmul(m1,m2):
    if len(m2)!=len(m1[0]):
        c='Invalid'
        return c
    m=[[0 for x in range(len(m2[0]))] for y in range(len(m1))]
    for i in range(len(m1)):
        for j in range(len(m2[0])):
            for k in range(len(m2)):
                m[i][j]+=m1[i][k]*m2[k][j]
    return m
