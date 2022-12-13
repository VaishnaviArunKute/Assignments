str = "Hi SaDer"
count = 0
for i in str:
    if i == " ":
        pass
    elif  i == i.upper():
        if i in str[0:4]:
            count += 1
            
    
if count == 2:
    print(str.upper())
else:
    print("you are dump")