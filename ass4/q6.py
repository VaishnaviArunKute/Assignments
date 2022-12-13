str = "string"
if len(str) < 3:
    print(str)
elif str[-3]=="i" and str[-2]=="n" and str[-1]=="g":
    str = str + "ly"
    print(str)
else:
    str = str + "ing"
    print(str)