class Solution(object):
    def removeDuplicates(self, nums):
        s = set()
        for i in nums:
            s.add(i)
        k=len(s)
        s=list(s)
        s.sort()
        for i in range(k):
            nums[i]=s[i]
        return k