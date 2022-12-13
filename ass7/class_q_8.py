class New:
    def __init__(self,string):
        self.string = string

    def get_string(self):
        #global string
        self.string = input("enter the string: ")
    
    def print_string(self):
        print(self.string)

e1 = New("hello")
e1.get_string()
e1.print_string()
