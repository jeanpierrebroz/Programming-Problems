class Solution:
    def checkSubarraySum(self, nums: List[int], k: int) -> bool:
        remainders = {0: -1}
        total = 0

        for idx, num in enumerate(nums):
            total += num
            remainder = total % k

            if remainder not in remainders:
                remainders[remainder] = idx
            
            elif idx - remainders[remainder] > 1:
                return True

        return False