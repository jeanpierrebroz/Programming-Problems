class Solution:
    def prefixCount(self, words: List[str], pref: str) -> int:
        n = len(pref)
        result = 0
        for word in words:
            if len(word) >= n and word[:n] == pref:
                result+=1
        
        return result
                