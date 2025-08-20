class Solution(object):
    def productExceptSelf(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        n = len(nums)
        arr = [1] * n
        
        # left pass
        left = 1
        for i in range(n):
            arr[i] = left
            left *= nums[i]
        
        # right pass
        right = 1
        for i in range(n - 1, -1, -1):
            arr[i] *= right
            right *= nums[i]
        
        return arr
