class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        cache = {}

        def backtrack(idx, path):
            if idx == len(nums):
                return 1 if path == target else 0

            if (idx, path) in cache:
                return cache[(idx, path)]
            
            
            
            cache[(idx, path)] = backtrack(idx + 1, path + nums[idx]) + backtrack(idx + 1, path - nums[idx])
        
            return cache[(idx, path)]

        return backtrack(0, 0)