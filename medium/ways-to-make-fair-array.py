class Solution:
    def waysToMakeFair(self, nums: List[int]) -> int:
        odd_sum, even_sum = 0, 0
        for i, num in enumerate(nums):
            if i % 2 == 0:
                even_sum += num
            else:
                odd_sum += num
        

        curr_even, curr_odd = 0, 0
        result = 0

        for i, num in enumerate(nums):
            
            if i % 2 == 0:
                even_sum -= num
            else:
                odd_sum -= num

            if curr_even + odd_sum == curr_odd + even_sum:
                result+=1

            if i % 2 == 0:
                curr_even += num
            else:
                curr_odd += num
        
        return result
            
            