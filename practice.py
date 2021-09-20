class methAccess:
    name="arun"
    def meth1(self):
        print(methAccess.name)

    def meth2(self):
        print(self.name)

obj = methAccess()
obj.meth1()
obj.meth2()