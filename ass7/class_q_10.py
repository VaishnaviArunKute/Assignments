class Myself:
    def __init__(self,fname,lname,age):
        self.fname = fname
        self.lname = lname
        self.age = age

    def into(self):
        print(f"my name is {self.fname} {self.lname} and I am {self.age} years old")

p1 = Myself("radha","thaore",21)
print(p1.__class__.__name__)