class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        num_map = {}
        for i, num in enumerate(nums):
            if num not in num_map or i - num_map[num] > k:
                num_map[num] = i
            else:
                return True
                
        return False