class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        min_length = float('inf')

        l = 0
        curr_sum = 0
        for r, num in enumerate(nums):
            curr_sum += num

            #if the current sum is >= target, shrink the window
            while curr_sum >= target and l <= r:
                min_length = min(min_length, r - l + 1)
                curr_sum -= nums[l]
                l += 1
        
        return min_length if min_length != float('inf') else 0
