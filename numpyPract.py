import numpy as np

class numClass:
    def meth1(self):
      arr = np.array([1,2,3,4])
      print(arr)

    def checkVersion(self):
        print(np.__version__)

    def ndarrmeth(self):
        arr1 = np.array(['apple','banana','orange'])
        print(type(arr1))
    def ndarrtuplearr(self):
        arr2=np.array((1,2,3,4,5))
        print(type(arr2))
    def finddimarrmeth(self):
        arr = np.array(1)
        arr2= np.array([1,2])
        arr3=np.array([[1,2],[1,3]])
        print("type of arr",arr.ndim)
        print("type of arr",arr2.ndim)
        print("type of arr",arr3.ndim)

        list1=[1,2,3,4]
        list1.append(5)
        print(list1)

obj = numClass()
obj.meth1()
obj.checkVersion()
obj.ndarrmeth()
obj.ndarrtuplearr()
obj.finddimarrmeth()