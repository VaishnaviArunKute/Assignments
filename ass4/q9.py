str = input("Enter the string: ")
let = int(input("Enter the letter to be removed: "))
list = list(str)
if bool(str) == False:
    print("plz enter non empty string")
else:
    for i in range(len(list)-1):    #counting from 0
        if i == let:
            list.pop(i)
x = "".join(list)
print(x)