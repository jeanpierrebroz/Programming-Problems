class Solution:
    def rob(self, nums: List[int]) -> int:
        #recurrence relation: max(current + i-1, next)
        n = len(nums)

        if n < 3:
            return max(nums)

        opt1, opt2 = nums[0], max(nums[0], nums[1])

        #this timed out, but useful for understanding how to solve recursively
        # def calculate_optimal_rob(idx: int):
        #     if idx >= n:
        #         return 0

        #     return max(nums[idx] + calculate_optimal_rob(idx+2), calculate_optimal_rob(idx+1))

        for i in range(2, n):
            t = max(nums[i] + opt1, opt2)

            opt1 = opt2
            opt2 = t
        
        return opt2