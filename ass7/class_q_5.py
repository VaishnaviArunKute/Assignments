class New:
    def __init__(self,array):
        self.array = array
        
    def check(self):    
        li = []
        for i in self.array:
            for j in self.array:
                for k in self.array:
                    a = i + j + k
                    if a == 0:
                        b = list((i,j,k))
                        li.append(b)
                        break
                                
        #print(li)
        
        m = li[0]
        new_list = list(([m]))
        for i in li:
            for j in i:
                k = new_list[-1]
                l = new_list[0]
                if j not in k and j not in l:
                    new_list.append(i)
                    break
                
        print(new_list)

a1 = New([-25, -10, -7, -3, 2, 4, 8, 10])
a1.check()