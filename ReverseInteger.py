class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        a=abs(x)
        s=str(a)
        rs=int(s[::-1])
        
        if a>2147483647 or rs>=2147483647:
            return 0
        
        else:
            if x>=0:
                s=str(x)
                return int(s[::-1])
            else:
                s=str(a)
                z=-int(s[::-1])
                return z
