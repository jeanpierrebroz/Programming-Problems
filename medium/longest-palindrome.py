class Solution:
    def longestPalindrome(self, s: str) -> str:
        #foreach index, just expand outward
        s = list(s)
        result = s[0]

        for i, char in enumerate(s):
            #start on this idx
            if i > 0:
                l, r = i-1, i
                while l > -1 and r < len(s) and s[l] == s[r]:
                    l -= 1
                    r += 1
                l += 1
                r -= 1
                if r - l + 1 > len(result):
                    result = s[l:r + 1]
            
            l, r = i, i

            while l > -1 and r < len(s) and s[l] == s[r]:
                l -= 1
                r += 1
            l += 1
            r -= 1
            if r - l + 1 > len(result):
                result = s[l:r + 1]


        
        return ''.join(result)