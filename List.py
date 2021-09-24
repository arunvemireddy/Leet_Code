class List:
    def meth(self):
        list=["arun","kumar"]
        y=list.index("arun")
        print(list)
        print(y)

        list1= [1,2,3,4,5,9,8,4,2,60,1,5,6]
        list1.sort()
        print(list1.pop(10))

obj = List()
obj.meth()