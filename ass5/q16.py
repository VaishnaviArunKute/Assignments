list = input("enter the list: ").split()
a = input("enter the word to be deleted: ")
for i in list:
    if i == a:
        list.remove(i)
    else:
        pass
print(list)