dic1={1:10, 2:20}
dic2={3:30, 4:40}
dic3={5:50, 6:60}

'''
dic4 = dic1.copy()
for key, value in dic2.items():  
    dic4[key] = value  
for key,value in dic3.items():
    dic4[key] = value 
'''

dic1.update(dic2)
dic1.update(dic3)
print(dic1)