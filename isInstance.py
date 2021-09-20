class isInstance:
    
    def meth1(self):
        print(isinstance(200.0,int))
    
    def meth2(self):
        print(isinstance(50.0,float))

    def __init__(self):
        self.meth1()
        self.meth2()

obj = isInstance()