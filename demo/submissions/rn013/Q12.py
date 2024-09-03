
def matmul(x, y):
    lst = []
    l = []
    a = x[0]
    if (len(a) == len(y)):  # Condition for matrices to be multipliable
        j = 0
        for j in range(0, len(x)):  # len(x) represents number of rows of x
            k = 0
            for k in range(0, len(y[0])):  # len(y[0]) represents number of columns in y
                sum = 0
                i = 0
                for i in range(0, len(x[0])):
                    sum = sum + x[j][i]*y[i][k]  # calculating each row at a time and appending to l

                lst.append(sum)
            l.append(lst)
            lst = []   # resetting lst to empty list in order to calculate new row
        return(l)

    else:
        return("Not Multipliable")

if __name__ == '__main__':
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
    y = []
    z = int(input())
    k = int(input())
    for i in range(z):
        # empty row
        row = []
        for j in range(k):
            # converts the input to int as the default one is string
            element = int(input())
            # appending the element to the 'row'
            row.append(element)
        # appending the 'row' to the 'matrix'
        y.append(row)

    print(matmul(x, y))

