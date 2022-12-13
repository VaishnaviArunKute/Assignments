li =  [('English', 88), ('Science', 90), ('Maths', 97), ('Social sciences', 82)]

a = lambda li : li[1]    

li.sort(key = a)
print(li)