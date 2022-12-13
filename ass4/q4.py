str = "restart"
list = list(str)
b = list.index("r",1,-1)
list[b] = "$"
z = "".join(list)
print(z)