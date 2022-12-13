list = [[10, 20], [40], [30, 56, 25], [10, 20], [33], [40]]
li = []
for i in list:
    if i not in li:
        li.append(i)
print(li)