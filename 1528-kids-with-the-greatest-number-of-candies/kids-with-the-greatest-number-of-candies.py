class Solution(object):
    def kidsWithCandies(self, candies, extraCandies):
        """
        :type candies: List[int]
        :type extraCandies: int
        :rtype: List[bool]
        """
        ret=[]
        high=max(candies)
        
        for candy in candies:
            if candy+extraCandies>=high:
                ret.append(True)
            else:
                ret.append(False)
        return ret