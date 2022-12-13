#only "India word is not working properly"

import random

f = open("ass8_2.txt","r")
#print(f.read())
list = []
for i in f:
    list.append(i)
    
list.remove(list[-1])
new_list = []
for x in list:
    new_list.append(x.replace("\n", ""))
#print(new_list)
a = random.choice(new_list)
t = a.lower()
print(t)
li = []
for i in range(len(t)):
    i = "_ "
    li.append(i)
#print(li)
raw_list = []



def guess():
    count = 0
    for j in range(1,14):
        w = input("guess the word: ")
        c = t.find(w)
        
        if w in t:
            li[c] = w
            global v
            v = "".join(li)
            print(v)
            if v == t:
                print("you guessed the word")
                break

        elif w not in t:
            count = count + 1
            print("Incorrect")
            print(f"you left with { 6 - count } chances to win ")
            if count >= 6:
                break

        else:
            pass

    
           
    if v == t:
        print("congrats you win the game")
    else:
        print("you loose the game, come on lets try again...")
        guess()            
    
    
guess()


