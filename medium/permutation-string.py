class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        #do we actually need to generate all permutations? I don't think so since we know both strings only contain lowercase letters
        target = [0] * 26
        for char in s1:
            target[ord(char) - ord('a')] += 1

        curr = [0] * 26

        s2 = list(s2)


        for i in range(len(s2)):
            curr[ord(s2[i]) - ord('a')] += 1
            if i < len(s1) - 1:
                continue
            
            if i > len(s1) - 1:
                curr[ord(s2[i - len(s1)]) - ord('a')] -= 1
            
            if curr == target:
                return True
        
        return False