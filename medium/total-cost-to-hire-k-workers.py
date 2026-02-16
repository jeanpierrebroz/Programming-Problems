import heapq
class Solution:
    def totalCost(self, costs: List[int], k: int, candidates: int) -> int:
        first = 0
        last = len(costs)-1
        first_heap = []
        last_heap = []
        total_cost = 0

        for _ in range(k):

            while len(first_heap) < candidates and first <= last:
                heapq.heappush(first_heap, costs[first])
                first+=1
                
            while len(last_heap) < candidates and first <= last:
                heapq.heappush(last_heap, costs[last])
                last-=1
            
            val1 = first_heap[0] if first_heap else float('inf')
            val2 = last_heap[0] if last_heap else float('inf')
            
            if val1 <= val2:
                total_cost += heapq.heappop(first_heap)
            else:
                total_cost += heapq.heappop(last_heap)
        
        return total_cost