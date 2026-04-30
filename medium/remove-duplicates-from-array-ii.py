class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return 1
        
        l = 0
        cnt = 1
        for i, num in enumerate(nums):
            if l < 2 or num != nums[l-2]:
                nums[l] = num
                l += 1
                    
        return l