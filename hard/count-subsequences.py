class Solution:
    def numDistinct(self, s: str, t: str) -> int:
        cache = {}
        def backtrack(idx, path, target_idx):
            if idx == len(s) or len(path) == len(t):
                if "".join(path) == t:
                    return 1
                return 0
            
            if (idx, target_idx) in cache:
                return cache[(idx, target_idx)]
            
            result = 0
            if s[idx] == t[target_idx]:
                path.append(s[idx])
                target_idx += 1
                result += backtrack(idx + 1, path, target_idx)
                path.pop()
                target_idx -= 1
            result += backtrack(idx + 1, path, target_idx)

            cache[(idx, target_idx)] = result

            return cache[(idx, target_idx)]
        
        return backtrack(0, [], 0)