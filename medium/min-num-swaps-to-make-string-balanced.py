class Solution:
    def minSwaps(self, s: str) -> int:
        size = 0
        for char in s:
            if char == "[":
                size += 1
            else:
                if size > 0:
                    size -= 1
        
        return (size + 1) // 2