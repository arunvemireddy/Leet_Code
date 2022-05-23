class Solution(object):
    def lengthOfLastWord(self, s):
        su = s.split()
        i = len(su)-1
        return len(su[i])
        """
        :type s: str
        :rtype: int
        """
        