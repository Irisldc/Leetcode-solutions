def longestCommonPrefix(strs):
    """
    :type strs: List[str]
    :rtype: str
    """
    lcp=''
    if not strs:
        return lcp
    else:
        shortest_str = min(strs, key=len)
        flag = 0
        for pos in range(len(shortest_str)):
            for s in strs:
                if s[pos]==shortest_str[pos]:
                    flag=0
                    continue
                else:
                    flag=1
                    break
            print pos,flag

            if flag==0:
                lcp+=shortest_str[pos]
            else:
                break

        return lcp
