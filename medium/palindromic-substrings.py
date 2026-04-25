class Solution:
    def countSubstrings(self, s: str) -> int:
        #given that the 
        #for each character, start l = r = idx. 
        #while bounds are valid and s[l] == s[r], expand out.
        result = 0

        # s = list(s)

        def expandOutward(l, r):
            count = 0
            while l > -1 and r < len(s) and s[l] == s[r]:
                count += 1
                l -=1
                r += 1
            
            return count

        for i in range(len(s)):
            result += expandOutward(i, i)
            result += expandOutward(i, i + 1)
        
        return result