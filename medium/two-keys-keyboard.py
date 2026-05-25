class Solution:
    def minSteps(self, n: int) -> int:
      
        cache = {}

        def backtrack(currChars, copiedChars):
            if currChars >= n:
                if currChars == n:
                    return 0
                return float('inf')
            elif (currChars, copiedChars) in cache:
                return cache[(currChars, copiedChars)]
            result = []
            if currChars == copiedChars:
                result.append(1 + backtrack(currChars + copiedChars, copiedChars))
            elif copiedChars == 0:
                result.append(1 + backtrack(currChars, currChars))
            else:
                result.append(1 + backtrack(currChars + copiedChars, copiedChars))
                result.append(1 + backtrack(currChars, currChars))

            cache[(currChars, copiedChars)] = min(result)
            
            return cache[(currChars, copiedChars)]
        return backtrack(1, 0)
