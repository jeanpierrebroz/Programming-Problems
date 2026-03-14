class Solution:
    def tupleSameProduct(self, nums: List[int]) -> int:
        
        pairs = {}
        total = 0
        
        for i in range(len(nums)):
            for j in range(i+1, len(nums)):
                product = nums[i] * nums[j]
                if product not in pairs:
                    pairs[product] = 1
                else:
                    pairs[product] += 1

        for freq in pairs.values():
            total += 8 * ((freq-1) * freq)//2
        
        return total