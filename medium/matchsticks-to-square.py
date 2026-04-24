class Solution:
    def makesquare(self, matchsticks: List[int]) -> bool:
        #find subsets (non-overlapping) where the subset == sum(matchsticks) // 4
        total = sum(matchsticks)

        if total % 4 != 0:
            return False
        
        matchsticks.sort(reverse=True)
        target = total // 4

        sides = [0, 0, 0, 0]

        def backtrack(idx):
            if idx == len(matchsticks):
                if sides[0] == sides[1] == sides[2] == sides[3] == target:
                    return True
                return False
            
            for j in range(4):
                if sides[j] + matchsticks[idx] <= target:
                    sides[j] += matchsticks[idx]
                    if backtrack(idx + 1):
                        return True
                    
                    sides[j] -= matchsticks[idx]
                    
                if sides[j] == 0:
                    break
            return False
        
        return backtrack(0)