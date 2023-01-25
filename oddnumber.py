class oddNum:
    def meth1(self,x):
        y = [1,2,3,4,5,6,7]
        print("method %d 1",x,end='')
        print(x)
        print(*y)
    
obj = oddNum()
obj.meth1(2)