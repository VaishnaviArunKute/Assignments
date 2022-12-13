class Circle:
    def __init__(self,radius):
        self.radius = radius
        

    def area(self):
        global pi
        pi = 3.142
        area_of_circle = pi * self.radius * self.radius
        print("area of circle: ", area_of_circle)

    def perimeter(self):
        perimeter_of_circle = 2 * pi *self.radius
        print("perimeter of circle",perimeter_of_circle)
    
p1 = Circle(6)
p1.area()
p1.perimeter()