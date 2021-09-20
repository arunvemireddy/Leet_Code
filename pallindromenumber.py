class Pallindrome:

    def __init__(self):
        print("hello world")
        self.meth1()

    def checkpallindrom(self,x):
        temp0=0
        while x>0:
            temp1=x%10
            temp1=int(temp1)
            # print(temp1)
            temp0=(temp0*10)+temp1
            x=x/10
            x=int(x)
        print(temp0)
    def meth1(self):
        inp=input()
        inp=int(inp)
        self.checkpallindrom(inp)

p= Pallindrome()