class A:
    
    def meth(self):
        print("from A")


class B(A):
    pass
    # def meth(self):
    #     print("from B")

obj1 = B()
obj1.meth()

class C:
    print("arun")

obj2 = C()