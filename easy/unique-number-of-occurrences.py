class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        #O(n) time, O(n) space
        count_dict = {}

        for num in arr:
            if num not in count_dict:
                count_dict[num] = 1
            else:
                count_dict[num] += 1
        
        counts = set()
        for count in count_dict.values():
            if count in counts:
                return False
            
            counts.add(count)
        
        return True