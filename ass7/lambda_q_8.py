
def check_string(str1):
    messg = [
    lambda str1: any(x.isupper() for x in str1) or 'String must have 1 upper case character.',
    lambda str1: any(x.islower() for x in str1) or 'String must have 1 lower case character.',
    lambda str1: any(x.isdigit() for x in str1) or 'String must have 1 number.',
    lambda str1: len(str1) >= 7                 or 'String length should be atleast 8.',]
    result = [x for x in [i(str1) for i in messg] if x != True]
    if not result:
        result.append('Valid string.')
    return result    
s = input("Input the string: ")
print(check_string(s))

'''
s = "PaceWis"
li = ['0','1','2','3','4','5','6','7','8','9']
a=b=c=d= " "
for i in s:
    if len(s) == 10:
        a = "True"
    if i == i.upper():
        b = "True"
    if i == i.lower():
        c = "True"
    if i in li:
        d = "True"
    else:
        pass

if a == "True" and b=="True" and c=="True" and d == "True":
    print("True")
else:
    print("False")
'''

