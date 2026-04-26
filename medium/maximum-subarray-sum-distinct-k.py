class Solution:
    def maximumSubarraySum(self, nums: List[int], k: int) -> int:
        result = 0
        count = defaultdict(int)
        curr_sum = 0

        l = 0

        for r, num in enumerate(nums):
            curr_sum += num
            count[num] += 1

            if r - l + 1 > k:
                back = nums[l]
                curr_sum -= back
                count[back] -= 1
                if count[back] == 0:
                    del count[back]
                l += 1
            
            if r - l + 1 == k == len(count):
                result = max(curr_sum, result)
        
        return result