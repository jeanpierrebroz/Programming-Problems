import heapq

class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        
        #minimum spanning tree problem
        def manhattan(p1: List[int], p2: List[int]):
            return abs(p1[0] - p2[0]) + abs(p1[1] - p2[1])

        n = len(points)
        if n ==1:
            return 0
        
        heap = [(0, 0)]
        in_mst = [False] * n

        total, added = 0, 0

        while added < n:
            cost, i = heapq.heappop(heap)
            if in_mst[i]:
                continue
            in_mst[i] = True
            total += cost
            added += 1

            xi, yi = points[i]
            for j in range(n):
                if not in_mst[j]:
                    xj, yj = points[j]
                    distance = manhattan(points[i], points[j])
                    heapq.heappush(heap, (distance, j))
        
        return total