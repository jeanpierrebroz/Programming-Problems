class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        result = []
        candidates.sort()

        def backtrack(idx, path, curr_sum):
            if curr_sum == target:
                result.append(list(path))
                return
            if idx == len(candidates) or curr_sum > target:
                return
            
            path.append(candidates[idx])
            backtrack(idx + 1, path, curr_sum + candidates[idx])
            path.pop()

            next_idx = idx + 1
            while next_idx < len(candidates) and candidates[next_idx] == candidates[idx]:
                next_idx += 1
            backtrack(next_idx, path, curr_sum)
        
        backtrack(0, [], 0)
        return result