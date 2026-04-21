class Solution:
    def partitionLabels(self, s: str) -> List[int]:

        hashmap = {}

        for i, char in enumerate(list(s)):
            hashmap[char] = i
         
        start = 0
        curr_end = 0
        result = []

        for i, char in enumerate(list(s)):
            curr_end = max(curr_end, hashmap[char])
            if i == curr_end:
                result.append(i - start + 1)
                start = i + 1

        return result            
    