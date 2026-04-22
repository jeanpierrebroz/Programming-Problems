class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]
        
        elif len(nums) == 2:
            return max(nums[0], nums[1])

        def rob(houses):
            prev1, prev2 = max(houses[1], houses[0]), houses[0]
            money = prev1
            for h in houses[2:]:
                money = max(prev1, prev2 + h)
                prev2 = prev1
                prev1 = money

            return money
        
        return max(rob(nums[1:]), rob(nums[:-1]))