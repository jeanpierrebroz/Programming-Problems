class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        #xor everything, the one at the end is the num
        result = nums[0]
        if len(nums) == 1:
            return result
        for num in nums[1:]:
            result ^= num
        return result