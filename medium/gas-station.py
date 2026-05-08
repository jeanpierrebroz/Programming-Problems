class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        #gas[i] is the amnt of gas at the ith station
        #cost[i] is the amnt of gas needed to travel from ith to ith + 1
        #at most 1 solution exists
        #brute force solution: try starting at every idx. if any one succeeds, return True
        #otherwise, return false
        # def simulate(start):
        #     n = len(gas)
        #     g = 0
        #     for i in range(0, n):
        #         idx = (start + i) % n
        #         g = g + gas[idx] - cost[idx]
        #         if g < 0:
        #             return False
        #     return True
        
        # for i in range(len(gas)):
        #     if simulate(i):
        #         return i
        # return -1

        if sum(cost) > sum(gas):
            return -1

        #this is inefficient tho.
        total = 0
        result = 0
        for i in range(len(gas)):
            total = total + gas[i] - cost[i]
            if total < 0:
                total = 0
                result = i + 1
        
        return result
                