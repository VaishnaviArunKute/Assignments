dic1={ 1:10, 2:60,
       3:70, 4:40,
       5:50, 6:90 }

x = list((dic1.values()))
x.sort(reverse = True)
print("highest 3 values in dictionary:",x[:3])