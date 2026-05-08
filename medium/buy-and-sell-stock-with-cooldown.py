class Solution:
    def maxProfit(self, prices: List[int]) -> int: 
        # we can either buy, sell, or do nothing on any given day
        # seems like this is a dp problem
        # with backtracking, this is O(3^n)
        # we could probably cache this. what uniquely identifies the state?
        # at any given call, we need to know if we currently have a coin, the index in the array and if we have a cooldown.
        cache = {}
        def backtrack(idx, haveNeetCoin, cooldown):
            if len(prices) == idx:
                return 0
                
            elif (idx, haveNeetCoin, cooldown) in cache:
                return cache[(idx, haveNeetCoin, cooldown)]
            options = []

            if not haveNeetCoin and cooldown == 0:
                options.append(-prices[idx] + backtrack(idx + 1, True, 0))
            if haveNeetCoin:
                options.append(prices[idx] + backtrack(idx + 1, False, 1))
            
            options.append(backtrack(idx + 1, haveNeetCoin, 0))
            cache[(idx, haveNeetCoin, cooldown)] = max(options)
            return cache[(idx, haveNeetCoin, cooldown)]
        
        return backtrack(0, False, 0)