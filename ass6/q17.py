dic1 = {'key1': 1, 'key2': 3, 'key3': 2}
dic2 = {'key1': 1, 'key2': 2}
#print(dic1.items())
for x in dic1.items():
    for y in dic2.items():
        if x == y :
            print("it is present in both dict1 and dict2 ",x)
            break
#else:
#   print("bye")