def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        if len(s)%2==1:
            return False
        
        while '()' in s or '{}' in s or '[]' in s:
            s=s.replace('{}','').replace('[]','').replace('()','')
        
        if s=='':
            return True
        else:
            return False
