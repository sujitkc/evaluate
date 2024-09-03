def transpose(m):
    r = len(m)
    for i in range(r):
        for j in range(i,r):
            m[i][j] , m[j][i] = m[j][i] , m[i][j]
    return m

if __name__ == "__main__":
    out=transpose([[1 , 2, 3] , [4 , 5, 6], [7, 8, 9]])
    print(out)
