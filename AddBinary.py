class Solution(object):
    def addBinary(self, a, b):
        ares=0
        bres=0
        result=0
        for index,i in enumerate(a[::-1]):
            i = int(i)
            ares=ares+(i*pow(2,index))
        
        for index,j in enumerate(b[::-1]):
            j = int(j)
            bres=bres+(j*pow(2,index))

        result=ares+bres
        div = result
       
        newresult=[]
        while div>0:
            rem = int(div%2)
            div = int(div/2)
            newresult.append(rem)
        r=''
        for k in newresult[::-1]:
            r=r+str(k)
        if len(r)==0:
            r="0"
        return r
                
        
        
        """
        :type a: str
        :type b: str
        :rtype: str
        """
        