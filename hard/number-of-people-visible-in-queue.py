class Solution:
    def canSeePersonsCount(self, heights: List[int]) -> List[int]:
        stack = []
        n = len(heights)
        result = []

        for i in range(n-1, -1, -1):
            height = heights[i]
            count = 0

            while stack and stack[-1] < height:
                stack.pop()
                count += 1
            
            if stack:
                count += 1

            stack.append(height)
            result.append(count)
        result.reverse()
        return result