class Check:
    def __init__(self,str):
        self.str = str
        
    def brackets(self):
        dic = { "(":")", "{":"}", "[":"]" }
        li = []
        if len(self.str) % 2 == 0:
            for i in self.str:      
                if i in  dic.keys():
                    x = dic[i]
                    if x not in self.str:
                        print("not valid")
                        break
                    else:
                        print("valid")
                        break
         
        else:
            print("not valid")
            
s1 = Check("{{{")
s1.brackets()