def mattrans(x):
    j = 0
    lst = []
    l = []
    for j in range(0, len(x[0])):  # j represents row of original matrix and i represents columns
        i = 0
        for i in range(0, len(x)):
            lst.append(x[i][j])  # j represents columns and i represents rows in new matrix, hence it is transpose
        l.append(lst)
        lst = []

    return(l)
if __name__ == '__main__':
    # initializing an empty matrix
    x = []
    a = int(input())
    b = int(input())
    for i in range(a):
        # empty row
        row = []
        for j in range(b):
            # converts the input to int as the default one is string
            element = int(input())
            # appending the element to the 'row'
            row.append(element)
        # appending the 'row' to the 'matrix'
        x.append(row)

    print(mattrans(x))