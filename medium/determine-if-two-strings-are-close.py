from collections import Counter

class Solution:
    def closeStrings(self, word1: str, word2: str) -> bool:
        #O(n) time + O(n) space, sorting is k log (k) where k is 26 bc it can only contain lowercase english letters
        if len(word1) != len(word2) or set(word1) != set(word2):
            return False
        
        c1 = Counter(word1)
        c2 = Counter(word2)
        
        return sorted(c1.values()) == sorted(c2.values())