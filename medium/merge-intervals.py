class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort()
        result = []
        curr_start, curr_end = intervals[0]
        for start, end in intervals:
            if curr_end < start:
                result.append([curr_start, curr_end])
                curr_start, curr_end = start, end
            
            else:
                curr_end = max(curr_end, end)
        
        result.append([curr_start, curr_end])
        return result

        