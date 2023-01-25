import re

class pallindromeValid:
    def meth1(self,x):
        x = x.lower()
        x = x.replace(" ","")
        my_new_string = re.sub('[^a-zA-Z0-9 \n\.]', '', x)
        print(my_new_string)
        print(my_new_string[::-1])
    
obj = pallindromeValid()
obj.meth1("a,")