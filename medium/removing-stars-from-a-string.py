class Solution:
    def removeStars(self, s: str) -> str:
        #O(n) time and space

        stack = []

        for char in s:
            if char != '*':
                stack.append(char)
            else:
                if stack:
                    stack.pop()
        
        return ''.join(stack)