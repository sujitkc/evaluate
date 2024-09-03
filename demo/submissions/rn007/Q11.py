def mattrans(lst):
  new_lst=[[0 for x in range(len(lst))] for y in range(len(lst[0]))]
  for i in range(len(lst)):       
    for j in range(len(lst[0])):
      new_lst[i][j]=lst[j][i]
  return (new_lst)    

if __name__=="__main__":
  lst=[[1,2,3],[4,5,6],[7,8,9]]
  new_lst=mattrans(lst)
  print(new_lst)

   
