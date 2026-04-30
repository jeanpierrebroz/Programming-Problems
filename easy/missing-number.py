class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        #however many numbers are in nums, keep a running sum
        #the running sum - actual sum(nums) should be the answer
        n = len(nums)

        s = 0
        for i in range(1, n + 1):
            s += i
        
        return s - sum(nums)