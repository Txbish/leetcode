class Solution(object):
    def canPlaceFlowers(self, flowerbed, n):
        """
        :type flowerbed: List[int]
        :type n: int
        :rtype: bool
        """
        i = 0
        length = len(flowerbed)
        
        while i < length and n > 0:
            if (flowerbed[i] == 0 and 
                (i == 0 or flowerbed[i-1] == 0) and 
                (i == length-1 or flowerbed[i+1] == 0)):
                flowerbed[i] = 1
                n -= 1
                i += 2  
            else:
                i += 1
        
        return n <= 0
