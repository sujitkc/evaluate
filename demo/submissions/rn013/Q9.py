def even_elements(l):
    lst = [x for x in l if (x % 2 == 0)] # taking only elements which give zero remainder apon division by two
    return(lst)

if __name__ == '__main__':
    lst = input().split(', ')
    i = 0
    for i in range(0, len(lst)):
        lst[i] = int(lst[i])

    print(even_elements(lst))