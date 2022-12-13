list = ["hii", 1, "hello", 1.5, 7, 9, "me", "i", 7.7, 15.321]
str_list = []
int_list = []
float_list = []
for i in list:
    if type(i) == str:
        str_list.append(i)
    elif type(i) == int:
        int_list.append(i)
    else:
        float_list.append(i)
print(str_list)
print(int_list)
print(float_list)
