class Solution(object):
    def romanToInt(self, s):
        x = str(s)
        nl = []
        res=[]
        for i in x:
            nl.append(i)
        for i in nl:
            if(i=='I'):
                res.append(1)
            if(i=="V"):
                res.append(5)
            if(i=='X'):
                res.append(10)
            if(i=='L'):
                res.append(50)
            if(i=='C'):
                res.append(100)
            if(i=='D'):
                res.append(500)
            if(i=='M'):
                res.append(1000)
        r=0
        i=0
        while i<len(res):
            if(i<len(res)-1):
                if res[i]<res[i+1]:
                    r=r+(res[i+1]-res[i])
                    i=i+2
                else:
                    r=r+res[i]
                    i=i+1
            else:
                r=r+res[i]
                i=i+1
        return r
            
        """
        :type s: str
        :rtype: int
        """
        