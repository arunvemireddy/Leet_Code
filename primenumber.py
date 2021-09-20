class primeNumber:
    num1=10
    str1="I am arun"
    def meth1(self,x):
        count=0
        print(type(x))
        for i in range(2,x-1):
            if (x % i)==0:
              count=count+1
              break
        if count==0:
            print("prime number yes")
            self.meth2()
        else:
            print("not a prime number")

    def meth2(self):
         z=input()
         print(self.num1)
         print(self.str1)
         self.meth1(int(z)) 



pn = primeNumber()

pn.meth2()