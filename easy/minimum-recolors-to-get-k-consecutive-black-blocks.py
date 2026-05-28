class Solution:
    def minimumRecolors(self, blocks: str, k: int) -> int:
        #sliding window of size k
        #keep track of how many black blocks there are in the window
        #return min of sliding window
        result = k
        black = 0

        for i, color in enumerate(blocks):
            if color == 'B':
                black += 1
            
            if i >= k - 1:
                if i >= k and blocks[i - k] == 'B':
                    black -= 1
                result = min(max(k - black, 0), result)
        
        return result