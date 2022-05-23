class Solution(object):
    def mySqrt(self, x):
        res=int()
        i=0
        while res<x:
            res=i*i
            if res==x:
                return i
            elif res<x:
                i=i+1
            else:
                return i-1
        return i