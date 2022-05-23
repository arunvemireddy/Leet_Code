class Solution:
    def meth(self,n):
        if n==1 or n==2:
            result = 1
        else:
            result = self.meth(n-1)+self.meth(n-2)
        return result

obj = Solution()
x=obj.meth(6)
print(x)