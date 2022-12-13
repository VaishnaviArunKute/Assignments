
is_num = lambda q: q.replace('.','',1).isdigit()
print(is_num('asdfe'))
print(is_num('4.2365'))
print(is_num('-12547'))
print(is_num('1234'))
is_num1 = lambda r: is_num(r[1:]) if r[0]=='-' else is_num(r)
print(is_num1('-16.4'))
print(is_num1('-24587.11'))

'''

mystr = '1234'
li = ['0','1','2','3','4','5','6','7','8','9']
for i in mystr:
    if i in li:
        if i == mystr[-1]:
            print("True")
        continue
    else:
        print("False")
        break

#last = list(filter(lambda mystr: print("True") if mystr in li else print("False"),mystr))

'''
