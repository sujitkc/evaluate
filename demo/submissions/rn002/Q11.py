def mattrans(lst):
    #creating an empty new_lst in a format to hold the transpose of lst
    new_lst=[[0 for x in range(len(lst))] for y in range(len(lst[0]))]

    for i in range(len(lst)):       #for every row 
        for j in range(len(lst[0])):#for every column 
                                    #interchange column and row and place them in new_lst
            new_lst[i][j]=lst[j][i]
    return (new_lst)    

if __name__=="__main__":
    print(mattrans([[1,2,3],[4,5,6],[7,8,9]]))

    # It should give  [[1,4,7],[2,5,8],[3,6,9]]
