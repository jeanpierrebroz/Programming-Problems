class Solution:
    def maxDifference(self, s: str) -> int:
        #count all unique ones
        frequencies = []
        s_list = list(s)

        unique = list(set(list(s)))

        for c in unique:
            frequencies.append(s_list.count(c))
        
        max_odd = 0

        min_even = float('inf')

        for num in frequencies:
            if num % 2 == 0:
                min_even = min(min_even, num)

            
            else:
                max_odd = max(max_odd, num)


        
        return max_odd - min_even