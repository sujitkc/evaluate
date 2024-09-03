def ndiamond(n):
    if n%2==0:
        print('Invalid Input')
    else:
        for i in range(1,int((n+3)/2)):
            for j in range(1,n-i):
                print(end=' ')
            for j in range(1,i+1):
                print(j,end='')
            for j in range(1,i):
                print(i-j,end='')
            print()
        for i in range(int((n-1)/2),0,-1):
            for j in range(1,n-i):
                print(end=' ')
            for j in range(1,i+1):
                print(j,end='')
            for j in range(1,i):
                print(i-j,end='')
            print()
