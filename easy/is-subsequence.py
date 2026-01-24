class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        #just see if we encounter them in the correct order
        #O(n) time, O(1) space

        i = j = 0

        while i < len(s) and j < len(t):
            if s[i] == t[j]:
                i+=1
            j+=1
        
        return i == len(s)