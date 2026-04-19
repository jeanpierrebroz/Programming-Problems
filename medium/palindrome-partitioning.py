class Solution:    
    def partition(self, s: str) -> List[List[str]]:
        def isPalindrome(s1):
            return s1 == s1[::-1]
        
        result = []

        palindrome_table = [[False for _ in range(len(s))] for _ in range(len(s))]

        for i in range(len(s)):
            for j in range(1, len(s)+1):
                palindrome_table[i][j-1] = isPalindrome(s[i:j])


        def backtrack(start, path):
            if start == len(s):
                result.append(list(path))
                return
                
            for end in range(start + 1, len(s) + 1):
                substr = s[start:end]
                if palindrome_table[start][end-1]:
                    path.append(substr)
                    backtrack(end, path)
                    path.pop()

            
        backtrack(0, [])
        return result