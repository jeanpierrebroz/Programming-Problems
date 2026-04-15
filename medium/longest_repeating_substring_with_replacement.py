class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        #how can we make the longest substring of the same letter, given we can change k letters?

        #k
        if len(s) == 1:
            return 1
        s = list(s)
        #current_start, current character, flips_used, result
        
        max_result = 0
        unique_chars = set(s)
        
        for char in unique_chars:
            l, r = 0, 0
            flips_used = 0
            curr_char = char
            while r < len(s):
                if s[r] == curr_char:
                    r += 1
                elif flips_used < k:
                    flips_used += 1
                    r += 1
                else:
                    if s[l] != curr_char:
                        flips_used -= 1
                    l += 1
                max_result = max(max_result, r - l)
        
        return max_result