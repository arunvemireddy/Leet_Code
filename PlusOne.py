class Solution(object):
    def plusOne(self, digits):
        st=''
        for i in digits:
            st = st+str(i)
        res = int(st)+1
        res = str(res)
        result=[]
        for j in res:
            result.append(int(j))
        return res
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        