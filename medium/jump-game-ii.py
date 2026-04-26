class Solution:
    def jump(self, nums: List[int]) -> int:
        jumps = 0
        currentEnd = 0
        farthest = 0
        n = len(nums)
        for i in range(n-1):
            farthest = max(farthest, i + nums[i])
            if i == currentEnd:
                jumps += 1
                currentEnd = farthest
                if currentEnd == n - 1:
                    break
            
        return jumps