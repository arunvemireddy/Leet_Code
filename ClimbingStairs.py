class Solution:
    def meth(self,n):
        one=1
        two=1
        for i in range(1,n-1):
            temp = one
            one = one + two
            two = one
        return one
obj = Solution()
x=obj.meth(5)
print(x)