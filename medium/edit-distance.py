class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        cache = {}
        def editDistance(i, j):
            if i == len(word1) or j == len(word2):
                if i == len(word1) and j == len(word2):
                    return 0
                return max(len(word1) - i, len(word2) - j)
            
            if (i, j) in cache:
                return cache[(i, j)]
            if word1[i] == word2[j]:
                cache[(i, j)] = editDistance(i + 1, j + 1)
            else:
                cache[(i, j)] = min(1 + editDistance(i + 1, j), 1 + editDistance(i, j + 1), 1 + editDistance(i + 1, j + 1))
            
            return cache[(i, j)]
        
        return editDistance(0, 0)