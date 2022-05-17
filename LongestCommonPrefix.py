class Solution(object):
    def longestCommonPrefix(self, strs):
        count=0
        j=1
        i=1
        s = set()
        if len(strs) == 1:
            return strs[0]

        for k in strs:
            if len(k)==0:
                return ""
        for c in strs:
            s.add(c)
        if len(s)==1:
            return strs[0]
            
        while i<len(strs):
            prefix = strs[0][0:j]
            if strs[i][0:j] == prefix:
                i=i+1
                if(i==len(strs)):
                    i=1
                    j=j+1
            else:
                
                break
        return strs[0][0:j-1]
                
                
            
        """
        :type strs: List[str]
        :rtype: str
        """
        