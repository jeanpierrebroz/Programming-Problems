class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        #cannot use division operation per problem statement
        #O(n) time complexity, O(1) space by calculating left prefix in result array and right prefix on the fly
        n = len(nums)
        result = [1] * n

        for i in range(1, n):
            result[i] = result[i-1] * nums[i-1]

        right_prefix = 1
        for i in range(n-1, -1, -1):
            result[i] *= right_prefix
            right_prefix *= nums[i]
        return result