def even_elements(l):
    lf=[]
    
    for i in l:
        if(i%2==0):
            lf.append(i)

    return lf

if __name__=="__main__":
    lst = even_elements ([0 , 1 , 2 , 3 , 4 , 5 , 6 , 7 , 8 , 9])
    print (lst)
