str1 = "abc"
str2 = "xyz"
a = str1[0:2]
b = str2[0:2]
str1 = str1.replace(a,b) 
str2 = str2.replace(b,a)
x = str1 + " " + str2
print(x)