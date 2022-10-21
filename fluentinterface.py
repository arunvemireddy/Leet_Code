class A:
    def __init__(self,n=0):
        self.n=n
        self.A(5).B(5).C()
    def A(self,n):
        self.n+=n
        self.B(2)
        return self

    def B(self,n,x="arun"):
        self.n+=n
        return self
    def C(self):
        print(self.n)

A()
# obj.A(5).B(5).C()

    
