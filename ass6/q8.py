dic1={ 1:10, 2:20,
       3:30, 4:40,
       5:50, 6:60 }
sum_x = 0
sum_y = 0
for x,y in dic1.items():
    sum_x += x
    sum_y += y
print(f"{sum_x} : {sum_y}")
