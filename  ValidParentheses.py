class Solution(object):
    def isValid(self, s):
        nl=[1]
        for i in range(len(s)):
            le = len(nl)
            if s[i]==')' and nl[le-1]=='(':
                nl.pop()
            elif s[i]==']' and nl[le-1]=='[':
                nl.pop()
            elif s[i]=='}' and nl[le-1]=='{':
                nl.pop()
            else:
                nl.append(s[i])
        if(len(nl)==1):
            return True
        else:
            return False
            
            
        
        """
        :type s: str
        :rtype: bool
        """
        