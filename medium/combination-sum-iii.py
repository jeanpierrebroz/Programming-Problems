class Solution:
    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        
        result = []
        def backtrack(start: int, remaining: int, path: List[int]):
            nums_needed = k - len(path)
            
            if nums_needed == 0:
                if remaining == 0:
                    result.append(path)
                return
            
            for i in range(start, 10):
                if i > remaining:
                    break
                
                backtrack(i + 1, remaining - i, path + [i])
        
        backtrack(1, n, [])
        return result