class Solution:
    def check(self, nums: List[int]) -> bool:
        #iterate thru nums. if we see a drop more than 1x, then return false. 
        
        if len(nums) == 1:
            return True
        
        flag = False
        for i in range(1, len(nums)):
            if nums[i] < nums[i - 1]:
                if flag:
                    return False
                flag = True

        if nums[-1] > nums[0] and flag:
            return False
        
        return True