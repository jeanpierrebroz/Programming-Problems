class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        cache = {}
        
        def largerSubsequence(idx, prevIdx):
            if (idx, prevIdx) in cache:
                return cache[(idx, prevIdx)]
            if idx == len(nums):
                return 0

            res = largerSubsequence(idx + 1, prevIdx)
            
            if prevIdx == -1 or nums[idx] > nums[prevIdx]:
                res = max(res, 1 + largerSubsequence(idx + 1, idx))
            
            cache[(idx, prevIdx)] = res
            return res
        
        import sys
        sys.setrecursionlimit(2000)
        return largerSubsequence(0, -1)