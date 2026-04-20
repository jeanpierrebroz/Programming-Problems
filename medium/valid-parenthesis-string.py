class Solution:
    def checkValidString(self, s: str) -> bool:
        stack = []
        star_indices = []

        for i, char in enumerate(s):
            if char == "*":
                star_indices.append(i)
            elif char == "(":
                stack.append(i)
            else:
                if stack:
                    stack.pop()
                elif star_indices:
                    star_indices.pop()
                else:
                    return False
            
        while stack and star_indices:
            if stack[-1] > star_indices[-1]:
                return False
            stack.pop()
            star_indices.pop()
            
        return not stack