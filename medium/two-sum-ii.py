class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        l, r = 0, len(numbers) - 1
        
        #need to remember that result is l + 1, r + 1
        while numbers[l] + numbers[r] != target:
            #if the current combo is too large, we need to move the right bound.
            if numbers[l] + numbers[r] > target:
                r -= 1
            #otherwise, update left bound
            else:
                l += 1
        return [l + 1, r + 1]