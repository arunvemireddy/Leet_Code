class A:
    def meth1(self):
        return "hello"

class B(A):
    def meth2(self):
        print(self.meth1())
        print("wordld")

class C(B):
    def meth3(self):
        self.meth2()
       
    #    return self.meth1()

Obj = C()
Obj.meth3()