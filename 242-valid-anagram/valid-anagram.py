from collections import Counter
class Solution:
    def isAnagram(self, s, t):
        if len(s)!=len(t):
            return False
        c1=Counter(s)
        c2=Counter(t)
        if c1==c2:
            return True
        return False