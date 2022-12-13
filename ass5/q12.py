class_held = int(input("enter the number of class held: "))
class_attended = int(input("enter the number of class attened: "))
a= (class_attended / class_held) * 100
print(int(a) , "%")
if a < 75:
    print("you are not allowed to sit in exam")
else:
    print("you are allowed to sit in exam")