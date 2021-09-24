class A:
    def meth1(self):
        return "hello"

class B(A):
    def meth2(self):
       print("wordld")
       print(self.meth1())
    #    return self.meth1()

Obj = B()
Obj.meth2()