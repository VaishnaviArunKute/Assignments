str = 'thequickbrownfoxjumpsoverthelazydog'
li = []
for i in str:
    if i not in li:
        li.append(i)
x = "".join(li)
print(x)

z = list(x)

for i in z:
   a = str.count(i)
   if a > 1:
    print(f"{i} : {a}")
