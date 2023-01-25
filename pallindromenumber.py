class Pallindrome:

    def __init__(self):
        print("Enter Number")
        self.meth1()

    def meth2(self,x):
        x = str(x)
        for i in x:
            print(i)

    def checkpallindrom(self,x):
        temp0=0
        while x!=0:
            temp1=x%10
            temp1=int(temp1)
            temp0=(temp0*10)+temp1
            x=x/10
            x=int(x)
        return temp0
        
    def meth1(self):
        inp=input()
        inp=int(inp)
        x = self.checkpallindrom(inp)
        if x == inp:
            print("is pallindrome")
        else:
            print("not pallindrome") 

p= Pallindrome()