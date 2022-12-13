li =  [19, 'red', 12, 'green', 'blue', 10, 'white', 'green', 1] 


a = list(filter(lambda li : type(li)==int,li))
a.sort()
b = list(filter(lambda li : type(li)==str,li))
b.sort()
a.extend(b)
print(a)