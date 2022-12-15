import matplotlib.pyplot as plt
'''
x = [1,-2,-1,-8,0,10]
y = [-2,4,-1,-3,4,-3]
plt.plot(x,y)
plt.xlabel('x - axis')
plt.ylabel('y - axis')
plt.title('My first graph!')
plt.show()
'''

Input =  [(1,-2), (-2, 4), (-1,-1),(-8, -3), (0, 4), (10,-3)]
Output=[]
for i in Input:
    new=[]
    for j in i:
        j=j+8
        new.append(j)
    Output.append(tuple(new))
print("the set of positive co-ordinates are: ",Output)

'''
x = [9,6,7,0,8,18]
y = [6,12,7,5,12,5]
plt.plot(x,y)
plt.xlabel('x - axis')
plt.ylabel('y - axis')
plt.title('My first graph!')
plt.show()
'''
