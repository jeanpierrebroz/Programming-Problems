class Solution:
    def areAlmostEqual(self, s1: str, s2: str) -> bool:
        c1, c2 = Counter(s1), Counter(s2)

        if s1 == s2:
            return True

        if len(s1) != len(s2) or c1 != c2:
            return False
        
        diff = 0

        for i in range(len(s1)):
            if s1[i] != s2[i]:
                diff += 1
        
        if diff == 2:
            return True
        
        return False