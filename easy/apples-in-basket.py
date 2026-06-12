class Solution:
    def maxNumberOfApples(self, weight: List[int]) -> int:
        #greedily take the smallest apple each time
        #do we have to sort? I think so
        weight.sort()
        result = 0
        curr = 0
        for w in weight:
            if curr + w < 5001:
                curr += w
                result += 1
            else:
                break
        
        return result