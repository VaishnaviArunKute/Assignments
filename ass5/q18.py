from q17 import even,odd

even.extend(odd)
list_3 = []
list_4 = []
list_5 = []
list_6 = []
list_7 = []
list_8 = []
list_9 = []
list_10 = []
for i in even:
    if i%10==0 :
        list_10.append(i)
      
    if i%9==0:
        list_9.append(i)

    if i%8==4:
        list_8.append(i)

    if i%7==0:
        list_7.append(i)

    if i%6==0:
        list_6.append(i)

    if i%5==0:
        list_5.append(i)

    if i%4==0:
        list_4.append(i)

    if i%3==0:
        list_3.append(i)
    else:
        pass


print("numbers divisible by 3: ",list_3)
print("numbers divisible by 4: ",list_4)
print("numbers divisible by 5: ",list_5)
print("numbers divisible by 6: ",list_6)
print("numbers divisible by 7: ",list_7)
print("numbers divisible by 8: ",list_8)
print("numbers divisible by 9: ",list_9)
print("numbers divisible by 10: ",list_10)
