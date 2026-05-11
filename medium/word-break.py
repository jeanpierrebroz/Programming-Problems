class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        cache = {}

        #what uniquely identifies my state here? why isn't begin and end enough?
        s = list(s)

        wordDict = set(wordDict)

        def calc(begin, end):
            if end == len(s):
                return end == begin
                
            if (begin, end) in cache:
                return cache[(begin, end)]

            result = huzz(begin, end + 1)
            if ''.join(s[begin: end + 1]) in wordDict:
               
                result = result or huzz(end + 1, end + 1)
            cache[(begin, end)] = result
            return cache[(begin, end)]
        
        return calc(0,0)
            
            