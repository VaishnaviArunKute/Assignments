class Unique_subset:
    def __init__(self,li):
        self.li = li 
        
    def operation(self):
        list_1 = []
        list_1.append(self.li)
        a = (len(self.li))
        for i in self.li:
            list_1.append(i)
            for j in self.li:
                if i != j:
                    b = list((i,j))
                    list_1.append(b)
            
        for i in list_1:
            if type(i) == int:
                b = [i]
                c = list_1.index(i)
                list_1[c] = b
        
            
        for i in list_1:
            if len(i) == 2:
                for j in list_1:
                    a = list((i[1],i[0]))
                    if j == a:
                        list_1.remove(j)
        
        print(list_1)

list1 = Unique_subset([4,5,6])
list1.operation()
    
