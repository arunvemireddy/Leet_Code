class Solution:
    def meth(self,n):
        if n==0 or n==1:
            return 1
        else:
            bottom_up=[None]*(n+1)
            bottom_up[1]=1
            bottom_up[2]=1
            for i in range(3,n+1):
                bottom_up[i]=bottom_up[i-1]+bottom_up[i-2]
            return bottom_up[n]
obj = Solution()
x=obj.meth(6)
print(x)
