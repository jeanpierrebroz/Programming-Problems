class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
    
        cache = {}

        def min_counts(idx, amount):
            if amount == 0:
                return 0

            elif (amount < 0 or idx == -1):
                return float("inf")
            
            elif (idx, amount) in cache:
                return cache[(idx, amount)]

            

            take = 1 + min_counts(idx, amount - coins[idx])
            skip = min_counts(idx - 1, amount)
            cache[(idx, amount)] = min(take, skip)
            return min(take, skip)

        result = min_counts(len(coins) - 1, amount)
        return result if result != float("inf") else -1