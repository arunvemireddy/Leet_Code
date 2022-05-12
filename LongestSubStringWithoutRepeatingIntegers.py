class Solution(object):
    def longestPalindrome(self, s):
        i=0
        j=i+1
        re=s[0]
        res=''
      
        if(s==s[::-1]):
            re=s
            return re
        else:
            while j<len(s):
                if s[i] == s[j]:
                    res = s[i:j+1]
                    j=j+1
                    if(res==res[::-1]):
                        if(len(res)>len(re)):
                            re=res
                    if(j==len(s)):
                        i=i+1
                        j=i+1
                else:
                    j=j+1
                    if(j==len(s)):
                        i=i+1
                        j=i+1
        return re