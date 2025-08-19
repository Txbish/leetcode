class Solution(object):
    def reverseWords(self, s):
        """
        :type s: str
        :rtype: str
        """
        a= re.findall(r"\b\w+\b", s)
        ret=""
        for x in a[:0:-1]:
            ret=ret.__add__(x)
            ret=ret.__add__(" ")
        ret=ret.__add__(a[0])
        
        return ret