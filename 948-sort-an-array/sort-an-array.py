from typing import List

class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        
        def mergeSort(arr, l, r):
            if l == r:
                return [arr[l]]   # base case: single element
            
            mid = (l + r) // 2
            left = mergeSort(arr, l, mid)
            right = mergeSort(arr, mid + 1, r)

            lc = 0
            rc = 0
            arrs = []
            while lc < len(left) and rc < len(right):
                if left[lc] < right[rc]:
                    arrs.append(left[lc])
                    lc += 1
                else:
                    arrs.append(right[rc])
                    rc += 1

            while lc < len(left):
                arrs.append(left[lc])
                lc += 1

            while rc < len(right):
                arrs.append(right[rc])
                rc += 1

            return arrs

        return mergeSort(nums, 0, len(nums) - 1)
