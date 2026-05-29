class Solution:
    def minGroups(self, intervals: List[List[int]]) -> int:
        result = 1

        count = defaultdict(int)
        for start, end in intervals:
            count[start] += 1
            count[end + 1] -= 1
            
        c = 0
        for key, val in sorted(count.items()):
            c += val
            result = max(c, result)
        return result
            
