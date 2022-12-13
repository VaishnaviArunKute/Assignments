thisdict = {1: 50, 2: 4, 3: 9, 4: 10, 5: 1}
x = max(thisdict, key= thisdict.get)

y = min(thisdict, key= thisdict.get)

print("max:",x)
print("min:",y)
