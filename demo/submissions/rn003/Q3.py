def border():
    for i in range (len(m)+3):
        print("*",end='')
    print("*")
    print("* ",end='')
    print(m,end='')
    print(" *")
    for i in range (len(m)+4):
        print("*",end='')
if __name__=="__main__":
    m=input()
    border()