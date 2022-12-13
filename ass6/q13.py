#not completed

dic1={ 1:10, 2:60,
       3:70, 4:60,
       5:50, 6:90 ,
       7:10, 8:50}
li = {}
for i,j in dic1.items():
  if j not in li.values():
    li.update({i:j})
  else:
    pass
  
print(li)