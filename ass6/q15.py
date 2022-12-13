d1 = {'a': 100, 'b': 200, 'c':300}
d2 = {'a': 300, 'b': 200, 'd':400}
thisdict = {}
for x,y in d1.items():
    for i,j in d2.items():
        if x == i:
            a=y+j
            thisdict.update({x:a})
            break
else:
    thisdict.update({i:j})
    thisdict.update({x:y})
print(thisdict)
            