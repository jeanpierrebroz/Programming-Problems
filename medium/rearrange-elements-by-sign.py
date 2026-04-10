from collections import deque
class Solution:
    def rearrangeArray(self, nums: List[int]) -> List[int]:
        #this could also be done w 2 pointers
        posDeq = deque()
        negDeq = deque()
        for num in nums:
            if num > 0:
                posDeq.append(num)
            
            else:
                negDeq.append(num)

            
        n = len(nums)

        for i in range(0, n, 2):
            nums[i] = posDeq.popleft()
            nums[i+1] = negDeq.popleft()
        
        return nums
