roman_table = {
    'I' : 1,
    'V' : 5,
    'X' : 10,
    'L' : 50,
    'C' : 100,
    'D' : 500,
    'M' : 1000,
}


class Integer_to_roman:
    def __init__(self,num):
        self.num=num

    def new(self):
        value = [1000,900,500,400,100,90,50,40,10,9,5,4,1]
        a = ["I","IV","V","IX","X","XL","L","XC","C","CD","D", "CM", "M"]
        symbol = a[::-1]
        roman_name = ""
        i = 0
        while self.num > 0:
            div  = self.num // value[i]
            self.num = self.num % value[i]
            while div :
                roman_name = roman_name + symbol[i]
                div = div -1
            i = i +1
        print(roman_name)
    
n1 = Integer_to_roman(49)
n1.new()


class Roman_to_integer:
    def __init__(self,s):
        self.s = s

    def r_to_i(self):
        number = 0
        last = "I"
        for i in self.s[::-1]:
            if roman_table[i] < roman_table[last]:
                number -= roman_table[i]
            else:
                number += roman_table[i]
            last = i
        print(number)  

s1 = Roman_to_integer("XXV")
s1.r_to_i()