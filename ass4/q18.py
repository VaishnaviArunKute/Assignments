str = "32.054,23"
list = list(str)
for i in list:
    if i == ".":
        x = list.index(i)
        a = i
    elif i == ",":
        y = list.index(i)
        b = i
    else:
        pass

list[2] = b
list[6] = a
z = "".join(list)
print(z)

 