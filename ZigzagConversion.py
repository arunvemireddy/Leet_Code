class Solution(object):
    def convert(self, s, numRows):
        if numRows==1:
            return s
        nl = []
        res=[]
        for i in s:
            nl.append(i)
        step = 2*numRows - 2
        for i in range(numRows):
            for j in range(i,len(s),step):
                res.append(s[j])
                if i!=0 and j+step-2*i < len(s) and i!=numRows-1:
                    res.append(s[j+step-2*i])
        newstr = ''.join(res)
        return newstr
                    
        """
        :type s: str
        :type numRows: int
        :rtype: str
        """
        