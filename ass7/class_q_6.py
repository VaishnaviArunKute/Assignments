class Power:
    def __init__(self,x,y):
        self.x = x
        self.y = y
    
    def first(self):
        a = pow(self.x,self.y)
        print(a)

p1 = Power(2,5)
p1.first()