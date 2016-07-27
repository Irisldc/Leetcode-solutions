def strStr(self, haystack, needle):
        """
        :type haystack: str
        :type needle: str
        :rtype: int
        """
        if needle=='':
            return 0
        d={}
        length=len(needle)
        if needle in haystack:
            for i in range(len(haystack)):
                d[i]=haystack[i]
    
        for key in d.keys():
            substr=''
            pos=key
            for l in range(length):
                substr+=d[pos]
                pos+=1
            if needle==substr:
                return key
        else:
            return -1
