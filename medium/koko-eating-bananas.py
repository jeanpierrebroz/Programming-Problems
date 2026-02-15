import math

class Solution:
    def minEatingSpeed(self, piles: list[int], h: int) -> int:
        lowest = 1
        highest = max(piles)
        res = highest 

        while lowest <= highest:
            mid = lowest + (highest - lowest) // 2
            
            total_time = 0
            for p in piles:
                total_time += math.ceil(p / mid)
            
            if total_time <= h:
                res = mid
                highest = mid - 1
            else:
                lowest = mid + 1
        
        return res