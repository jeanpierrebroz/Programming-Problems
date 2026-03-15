class Solution:
    def findLongestChain(self, pairs: List[List[int]]) -> int:
        pairs.sort(key=lambda x: x[1])

        chains = 0

        prev_b = -1001

        for pair in pairs:
            a = pair[0]
            b = pair[1]

            if a > prev_b:
                prev_b = b
                chains+=1
        
        return chains
