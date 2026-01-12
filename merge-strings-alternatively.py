class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        
        ''' 
        naive approach: O(m+n) space, O(m*n) time complexity b/c of string 
        immutability

        l1, l2 = len(word1), len(word2)
        result = ""

        for i in range(min(l1, l2)):
            result += word1[i]
            result += word2[i]

        if l1 > l2:
            result += word1[i+1:]
            return result
        
        elif l2 > l1:
            result += word2[i+1:]

        return result

        '''

        #optimized: use list for O(n) time instead
        l1, l2 = len(word1), len(word2)
        result = []

        for i in range(min(l1, l2)):
            result.append(word1[i])
            result.append(word2[i])
        
        if l1 > l2:
            result.extend(word1[l2:]) 
        else:
            result.extend(word2[l1:]) 

        return ''.join(result)