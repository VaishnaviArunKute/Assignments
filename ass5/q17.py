even =[]
odd = []
prime= []

for i in range(1,101):
    for j in range(2,i):
        if i % j == 0:
            break
    else:
        prime.append(i)

#print("prime: ",prime)

for i in range(1,101):
    if i % 2 == 0:
        even.append(i)
    elif i % 2 == 1:
        odd.append(i)
    else:
        pass
       
#print("even: ",even)
#print("odd: ", odd)



 

'''
n = 6
for i in range(2,n):
    if n % i == 0:
        print("not prime")
        break
else:
    print("prime")
'''