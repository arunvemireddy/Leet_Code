class HappyNumber:
    def meth1(self,x):
        x = str(x)
        sum=0
        while True:
            sum=0
            for i in x:
                i = int(i)
                sum = sum + i*i
            x=sum
            if x==1:
                break
            x=str(x)
            print(sum)
            

obj = HappyNumber()
obj.meth1(20)