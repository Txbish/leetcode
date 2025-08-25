from typing import List

class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        
        def mergeSort(nums, temp, l, r):
            if l >= r:
                return
            
            mid = (l + r) // 2
            mergeSort(nums, temp, l, mid)
            mergeSort(nums, temp, mid + 1, r)
            merge(nums, temp, l, mid, r)

        def merge(nums, temp, l, mid, r):
            # copy the range into temp
            for i in range(l, r + 1):
                temp[i] = nums[i]

            i, j = l, mid + 1
            k = l

            while i <= mid and j <= r:
                if temp[i] <= temp[j]:
                    nums[k] = temp[i]
                    i += 1
                else:
                    nums[k] = temp[j]
                    j += 1
                k += 1

            while i <= mid:
                nums[k] = temp[i]
                i += 1
                k += 1

            # No need for "while j <= r": right half is already in place

        n = len(nums)
        temp = [0] * n  # one reusable buffer
        mergeSort(nums, temp, 0, n - 1)
        return nums
