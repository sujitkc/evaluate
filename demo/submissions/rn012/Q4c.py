def diamond(n,c):
    if n%2==0:
        print('Invalid Input')
    else:
        for i in range(1,int((n+3)/2)):
            for j in range(1,(n-i-2)*len(c)+1):
                print(end=' ')
            for j in range(1,2*i):
                print(c,end='')
            print()
        for i in range(int((n-1)/2),0,-1):
            for j in range(1,(n-i-2)*len(c)+1):
                print(end=' ')
            for j in range(1,2*i):
                print(c,end='')
            print()
