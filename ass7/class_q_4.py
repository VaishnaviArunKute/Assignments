class FindIndex:
    def __init__(self,numbers,target) :
        self.numbers = numbers
        self.target = target

    def find(self):
        for i in self.numbers:
            for j in self.numbers:
                if i + j == self.target:
                    a = i
                    b = j
                    break

        for k in range(len(self.numbers)-1):    
            if self.numbers[k] == a:
                print(k+1)
            elif self.numbers[k] == b:
                print(k+1)
            else:
                pass
    
numbers= [90,20,10,40,50,60,70]
target=50
e1 = FindIndex(numbers,target)
e1.find()
