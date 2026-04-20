class Solution:
    def validPalindrome(self, s: str) -> bool:
        s = list(s)
        l, r = 0, len(s)-1
        deleted = False
        diff1, diff2 = 0, 0

        #record indices of first discrepancy, just check both resulting palindromes

        while l < r:
            if s[l] != s[r]:
                diff1, diff2 = l, r
                break
            r-=1
            l+=1

        if l >= r:
            return True
        
        l1, l2 = [], []

        for i, char in enumerate(s):
            if i != diff1:
                l1.append(char)
            if i != diff2:
                l2.append(char)
        
        return l1 == list(reversed(l1)) or l2 == list(reversed(l2))