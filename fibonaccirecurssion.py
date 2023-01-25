class Solution:
    def __init__(self):
        print("enter number")
        x = input()
        x = int(x)
        res = self.meth(x)
        print(res)

    def meth(self,n):

        if n==0:
            result = 0

        if n==1 or n==2:
            result = 1
        else:
            result = self.meth(n-1)+self.meth(n-2)
            
        return result

obj = Solution()


