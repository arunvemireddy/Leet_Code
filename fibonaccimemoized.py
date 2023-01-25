class Solution:
    def meth(self,n,memo):
        if n in  memo:
            result = memo[n]
        elif n==0 or n==1:
            result = 1
        else:
            result = self.meth(n-1,memo)+self.meth(n-2,memo)
            memo[n]=result
            print(memo[n],end='')
        return result


obj = Solution()
n=7
mem=[None]*(n)
x=obj.meth(n-1,mem)
print('')
print( x)




