list = input("Enter the list of words: ").split(",")
list.sort()
print(list)
li = []
for i in list:
    if i not in li:
        li.append(i)
x = " ".join(li)
print(x)
