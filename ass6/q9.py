dic1={ 1:10, 2:20,
       3:30, 4:40,
       5:50, 6:60 }
multiply_x = 1
multiply_y = 1
for x,y in dic1.items():
    multiply_x *= x
    multiply_y *= y
print(f"{multiply_x} : {multiply_y}")
