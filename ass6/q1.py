thisdict = {
  "color1": "purple",
  "model": "yellow",
  "color" : "red"
}

x = list((thisdict.values()))
y = sorted(x)
x.sort(reverse = True)
print("descending: ",x)
print("ascending: ",y)

