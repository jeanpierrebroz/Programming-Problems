class Solution:
    def shortestDistance(self, wordsDict: List[str], word1: str, word2: str) -> int:
        start = -1
        result = float('inf')
        for i, word in enumerate(wordsDict):
            if word == word1:
                start = i
            elif word == word2 and start != -1:
                result = min(i - start, result)
        start = -1
        for i, word in enumerate(reversed(wordsDict)):
            if word == word1:
                start = i
            
            elif word == word2 and start != -1:
                result = min(result, i - start)
        
        return result
