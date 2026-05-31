class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        r = sum(nums)
        l = 0
        if len(nums) == 1:
            return 0
            
        for i, num in enumerate(nums):
            r -= num
            if l == r:
                return i
            l += num

        return -1