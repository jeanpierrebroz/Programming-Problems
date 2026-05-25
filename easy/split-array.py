class Solution:
    def isPossibleToSplit(self, nums: List[int]) -> bool:
        counter = defaultdict(int)
        for n in nums:
            if counter[n] == 2:
                return False
            counter[n] += 1
        return True