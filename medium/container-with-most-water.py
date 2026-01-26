class Solution:
    def maxArea(self, height: List[int]) -> int:
        #O(n) time, O(1) space
        begin, end = 0, len(height)-1
        
        maxWater = 0

        while begin < end:
            currWater = min(height[begin], height[end]) * (end-begin)
            maxWater = max(maxWater, currWater)

            if height[end] > height[begin]:
                begin+=1
            else:
                end-=1

        return maxWater