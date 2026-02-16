class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        digit_map = {2: "abc", 3: "def", 4: "ghi", 5: "jkl", 6: "mno", 7: "pqrs", 8: "tuv", 9: "wxyz" }
        result = []
        def combinations(remaining_chars: str, curr_string: str):
            if len(curr_string) == len(digits):
                result.append(curr_string)
                return
            
            for char in digit_map[int(remaining_chars[0])]:   
                combinations(remaining_chars[1:], curr_string + char)         
        
        combinations(digits, "")
        return result