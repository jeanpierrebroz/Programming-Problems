class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        #O(n) time, O(1) space
        total = sum(nums)
        tracker = 0

        for i, num in enumerate(nums):
            if tracker == total - tracker - num:
                return i
            tracker+=num
        return -1