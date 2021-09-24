class Forloop:

    def meth(self,step):
        step=int(step)
        for i in range(0,10,step):
            print("Hello")
            self.step=2
        
obj = Forloop()
obj.meth(1)