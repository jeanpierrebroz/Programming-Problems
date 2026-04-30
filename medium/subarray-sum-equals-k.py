class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        s = 0
        result = 0
        frequencies = defaultdict(int)
        frequencies[0] = 1

        for num in nums:
            s += num
            diff = s - k
            result += frequencies[diff]
            frequencies[s] += 1
        return result