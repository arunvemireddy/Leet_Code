class Solution(object):
    def merge(self, nums1, m, nums2, n):
        for i in nums2:
            for index,j in enumerate(nums1):
                if nums1[index] == 0:
                    nums1[index]=i
                    nums1.sort()
                    break
        """
        :type nums1: List[int]
        :type m: int
        :type nums2: List[int]
        :type n: int
        :rtype: None Do not return anything, modify nums1 in-place instead.
        """
        