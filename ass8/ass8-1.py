#digit is repeting

import random

def num_generator():            
    a = random.randrange(0, 10)
    b = random.randrange(0, 10)
    c = random.randrange(0, 10)
    d = random.randrange(0, 10)
    if a != b or b != c or c != d or d != a:
        global e
        e =str(a)+str(b)+str(c)+str(d)
        e = '1234'
        print(e)  
    else:
        num_generator() 

num_generator() 

'''
if a == b or b == c or c == d or d == a:
    b = random.randrange(0, 10)
if a == b or b == c or c == d or d == a:
    c = random.randrange(0, 10)
if a == b or b == c or c == d or d == a:
    d = random.randrange(0, 10)

e =str(a)+str(b)+str(c)+str(d)
print(e)
'''

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
                    
            else:
                x = "bull"
                #print(x)
                if x == "bull" :
                    count_bull += 1
                    #print("bull: ",count_bull)
        print(f"{count_cow} cows, {count_bull} bulls")
        count_bull = 0
        count_cow = 0


