class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        #we have n numbers to choose from, and can make k choices
        result = []

        def combinations(idx, choicesRemaining, path):
            if idx > n or choicesRemaining == 0:
                if choicesRemaining == 0:
                    result.append(list(path))
                return
            
            
            path.append(idx)
            combinations(idx + 1, choicesRemaining - 1, path)
            path.pop()
            combinations(idx + 1, choicesRemaining, path)
        
        combinations(1, k, [])
        return result