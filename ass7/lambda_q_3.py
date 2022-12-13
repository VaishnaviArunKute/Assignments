my_dict =   [{'make': 'Nokia', 'model': 216, 'color': 'Black'}, {'make': 'Mi Max', 'model': '2', 'color': 'Gold'}, {'make': 'Samsung', 'model': 7, 'color': 'Blue'}]

dic = lambda item: item['color']  

my_dict.sort(key = dic)
print(my_dict)