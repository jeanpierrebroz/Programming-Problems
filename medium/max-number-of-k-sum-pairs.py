class Solution:
    def maxOperations(self, nums: List[int], k: int) -> int:
        value_dict = {}
        max_ops = 0

        for num in nums:
            target = k - num
            if value_dict.get(target, 0) > 0:
                max_ops += 1
                value_dict[target] -= 1
            else:
                value_dict[num] = value_dict.get(num, 0) + 1
        
        return max_ops        