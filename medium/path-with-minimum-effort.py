class Solution:
    def minimumEffortPath(self, heights: List[List[int]]) -> int:
        #A route's effort is the max absolute diffs in heights between 2 consecutive cells of the route
        #use dijkstra's with edge weights being the effort instead of the path length

        if len(heights) == 1 and len(heights[0]) == 1:
            return 0
        N, M = len(heights), len(heights[0])
        q = [(0, 0, 0)]
        efforts = {}

        while q:
            effort, i, j = heapq.heappop(q)
            if (i, j) in efforts:
                continue
            efforts[(i, j)] = effort
            d = [(0, 1), (1, 0), (-1, 0), (0, -1)]
            for di, dj in d:
                ni, nj = di + i, dj + j
                if 0 <= ni < len(heights) and 0 <= nj < len(heights[0]) and (ni, nj) not in efforts:
                    heapq.heappush(q, (max(abs(heights[i][j] - heights[ni][nj]), effort), ni, nj))

                
        
        return efforts[(N-1, M-1)]


