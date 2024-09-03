def double(l):
    lst = [x*2 for x in l]
    return(lst)

if __name__ == '__main__':
    lst = input().split(', ')
    i = 0
    for i in range(0, len(lst)):
        lst[i] = int(lst[i])

    print(double(lst))
