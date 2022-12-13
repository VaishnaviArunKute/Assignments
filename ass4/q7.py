str =  'The lyrics is not that poor!'
a = str.find("not")
b = -1
c = str[a:b]
if "not" and "poor" in str:
    z = str.replace(c,"good")
print(z)