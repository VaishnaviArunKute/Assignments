class Reverse:
    def __init__(self, string):
        self.string = string

    def myfunc(self):
        self.string = self.string.split(" ")
        new_list = list(self.string[::-1])
        d = " ".join(new_list)
        print(d) 

s1 = Reverse(" geeks quiz practice code")
s1.myfunc()