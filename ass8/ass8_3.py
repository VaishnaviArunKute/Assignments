str = "[(])}"
dic = { "(":")", "{":"}", "[":"]" }
li = []
    
if len(str) % 2 == 0:
    for i in str:      
        if i in  dic.keys():
            li.append(i)
            x = dic[i]
        if i in dic.values():
            #x = dic[i]
            z = li[-1]
            if dic[z] == i:
                li.remove(z)
            else:
                pass
    if bool(li) == False:
        print("True")
    else:
        print("False")
else:
    print("false")

