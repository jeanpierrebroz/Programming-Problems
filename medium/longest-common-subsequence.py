class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        if text1 == text2:
            return len(text1)
        elif text1 in text2:
            return len(text1)
        elif text2 in text1:
            return len(text2)
        
        cache = {}

        def backtrack(idx1, idx2):
            if idx1 == len(text1) or idx2 == len(text2):
                return 0
            
            elif (idx1, idx2) in cache:
                return cache[(idx1, idx2)]
            
            res = 0
            if text1[idx1] == text2[idx2]:
                res = 1 + backtrack(idx1 + 1, idx2 + 1)
            
            cache[(idx1, idx2)] = max(res, backtrack(idx1 + 1, idx2), backtrack(idx1, idx2 + 1))

            return cache[(idx1, idx2)]
            

        
        return backtrack(0, 0)