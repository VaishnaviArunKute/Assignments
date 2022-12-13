n = int(input("Enter the number: "))
dic = {}
for i in range(1,n+1):
    dic.update({i : i*i})
print(dic)