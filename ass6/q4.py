dic = {
    "name" : "Radha",
    "Roll no" : 7,
    "address" : "Pune"
}

key = input("enter the key you want to search: ")
if key in dic.keys():
    print("the key is in dictionery")
else:
    print("the key is not in dictionery")