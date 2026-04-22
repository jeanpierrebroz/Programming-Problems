class Solution:
    def combinationSum4(self, nums: List[int], target: int) -> int:
        
        memo = {}
        def backtrack(currSum):
            if currSum == target:
                return 1
            if currSum > target:
                return 0
            if currSum in memo:
                return memo[currSum]
            
            res = 0
            for i in range(len(nums)):
                res += backtrack(currSum + nums[i])
            
            memo[currSum] = res
            return res

        return backtrack(0)