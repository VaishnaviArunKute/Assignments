list =[]
for i in range(1, 100):
    integer = int(input("enter the integer: "))
    list.append(integer)
    for_quit = input("enter q to quit: ")
    for_quit = for_quit.lower()
    if for_quit == "q":
        break
    else:
        pass

prod = 1
sum = 0
for i in list:
    prod *= i
    sum += i
print("product: ",prod)
print("average: ",sum/len(list))



