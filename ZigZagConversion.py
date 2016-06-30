class Solution(object):
    def convert(self, s, numRows):
        """
        :type s: str
        :type numRows: int
        :rtype: str
        """
        
        str = ''
        d = {}
        t=2*numRows-2
        
        if len(s)<=numRows or numRows==1:
            return s
        else:
            #initialize a dictionary
            for i in range(0,numRows):
                d[i]=""
            
            for j in range (len(s)):
                k=j%t
                if k<numRows:
                    temp=d[k]+s[j]
                    d[k]=temp
        
                elif k>=numRows:
                    n=(numRows-1)-(k-(numRows-1))
                    temp=d[n]+s[j]
                    d[n]=temp
        
            for key in d.keys():
                str+=d[key]
       
        return str
