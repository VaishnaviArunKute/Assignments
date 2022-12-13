list = []
for i in range(1,11):
    a = int(input(f"enter {i}st number: "))
    list.append(a)
sum = 0
for i in list:
    sum += i
print("average of numbers : ",sum / 10)

