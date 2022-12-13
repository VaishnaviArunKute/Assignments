mylist =  [19, 65, 57, 39, 152, 639, 121, 44, 90, 190] 
newlist = list(filter(lambda mylist : mylist % 13 == 0 or mylist % 19 == 0,mylist))
print(newlist)