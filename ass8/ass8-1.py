

import random
li=[]
def num_generator():            
    a = random.randrange(1000, 9999)
    a = str(a)
    for i in a:
        li.append(i)
    
num_generator() 
#print(li)

li2=[]
for i in li:
    if i not in li2:
        li2.append(i)
    else:
        num_generator() 

#print(li2)
e = ''.join(li2)
print(e)



count_bull = 0
count_cow = 0

print("Welcome to the Cows and Bulls Game! ")
for j in range(1,1000):
    num = input("Enter four digit number: ")
    if num == e:
        print("Congrats! you guessed the number correct ")
        print(f"you take {j} chances to guess the number")
        break
    else:
        for i in range(len(num)):
            #print(num[i],i)
            #print(e[i],i)
            if num[i] == e[i] and i == i:
                x = "cow"
                #print(x)
                if x == "cow":
                    count_cow += 1 
                    #print("cow: ",count_cow)
                    
            elif num[i] in li2:
                x = "bull"
                #print(x)
                if x == "bull" :
                    count_bull += 1
                    #print("bull: ",count_bull)
            else:
                pass
        print(f"{count_cow} cows, {count_bull} bulls")
        count_bull = 0
        count_cow = 0


