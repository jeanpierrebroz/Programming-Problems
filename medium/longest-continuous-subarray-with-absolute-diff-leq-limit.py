class Solution:
    def longestSubarray(self, nums: List[int], limit: int) -> int:
        minheap, maxheap = [], []

        result = 1

        start = 0

        for i, num in enumerate(nums):
            heapq.heappush_max(maxheap, (num, i))
            heapq.heappush(minheap, (num, i))

            while abs(maxheap[0][0] - minheap[0][0]) > limit:
                start += 1
                while minheap and minheap[0][1] < start:
                    heapq.heappop(minheap)
                while maxheap and maxheap[0][1] < start:
                    heapq.heappop_max(maxheap)
            
            result = max(result, i - start + 1)
        
        return result