class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        if sum(nums) % 2 == 1 or len(nums) == 1 or max(nums) > sum(nums) // 2:
            return False
        
        target = sum(nums) // 2
        nums.sort()

        #0/1 knapsack exactly

        #at each idx, we can either include or not include the number
        #we can end up at the same cache idx, path combo multiple times 
        cache = {}

        def backtrack(idx, path):

            if (idx, path) in cache:
                return cache[(idx, path)]

            if idx == len(nums):
                return -1
            elif path == target:
                return 0
            elif nums[idx] + path > target:
                return -1
            
            
            cache[(idx, path)] = max(backtrack(idx + 1, path + nums[idx]), backtrack(idx + 1, path))

            return cache[(idx, path)]

        return backtrack(0, 0) == 0