class Solution:
    def kthDistinct(self, arr: List[str], k: int) -> str:
        counts = defaultdict(int)
        for s in arr:
            counts[s] += 1
        
        for key, val in counts.items():
            if val == 1:
                k -= 1
                if k == 0:
                    return key
        return ""