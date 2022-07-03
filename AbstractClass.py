import abc

class A(abc.ABC):
  

    def meth1(self):
        print("concrete method")

class B(A):

    def meth1(self):
        self.meth1()
        print(2+2)

obj = B()
obj.meth1()