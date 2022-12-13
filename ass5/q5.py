n = int(input("enter the number: "))
sum = 0
if n == 0:
    print("finish")
else:
    for i in range(0,n+1):
        sum = sum + i
    print(f"sum = {sum}")
    avg = sum / n
    print(f"average = {avg}")
