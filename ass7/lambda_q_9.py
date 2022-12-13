mylist = ['red', 'black', 'white', 'green', 'orange']
s = input("enter the string: ")
a = list(filter(lambda mylist : s in mylist,mylist))
print(a)