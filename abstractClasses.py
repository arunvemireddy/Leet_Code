import abc

class MyAbstractClass(abc.ABC):
     @abc.abstractmethod
     def fun(self):
         pass

class MyClass(MyAbstractClass):
    def fun(self):
        print("Hello")

obj = MyClass()

obj.fun()