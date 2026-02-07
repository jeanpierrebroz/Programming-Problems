class Solution:
    def guessNumber(self, n: int) -> int:
        low = 1
        high = n
        
        while low <= high:
            mid = low + (high - low) // 2
            res = guess(mid)
            
            if res == 0:
                return mid
            elif res == 1:
                low = mid + 1
            else:
                high = mid - 1