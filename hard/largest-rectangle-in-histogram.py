class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:

        curr_max = max(heights)

        stack = []

        for i, height in enumerate(heights):
            if not stack:
                stack.append(i)
                continue
            
            while stack and heights[stack[-1]] > heights[i]:
                idx = stack.pop()
                height = heights[idx]
                left_bound = stack[-1] if stack else -1
                width = i - left_bound - 1
                curr_max = max(curr_max, height * width)
            
            stack.append(i)
        while stack:
            idx = stack.pop()
            height = heights[idx]
            left_bound = stack[-1] if stack else -1
            width = i - left_bound
            curr_max = max(curr_max, height * width)
        return curr_max