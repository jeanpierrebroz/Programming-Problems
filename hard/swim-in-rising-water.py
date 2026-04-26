class Solution:
    def swimInWater(self, grid: List[List[int]]) -> int:

        class GridPoint:
            def __init__(self, r, c, curr_max):
                self.row = r
                self.col = c
                self.curr_max = curr_max

            def __lt__(self, other):
                return self.curr_max < other.curr_max

            def getNeighbors(self, n):
                directions = [(0, 1), (1, 0), (-1, 0), (0, -1)]
                neighbors = []
                for dr, dc in directions:
                    nr, nc = self.row + dr, self.col + dc
                    if 0 <= nr < n and 0 <= nc < n:
                        neighbors.append((nr, nc))
                return neighbors

        heap = [GridPoint(0, 0, grid[0][0])]
        n = len(grid)
        visited = set()
        visited.add((0, 0))

        if len(grid[0]) == 1:
            return 0

        while heap:
            curr = heapq.heappop(heap)
            row, column, curr_max = curr.row, curr.col, curr.curr_max

            if row == n - 1 and column == n - 1:
                return curr_max

            for nextrow, nextcolumn in curr.getNeighbors(n):
                if (nextrow, nextcolumn) not in visited:
                    visited.add((nextrow, nextcolumn))
                    next_max = max(curr_max, grid[nextrow][nextcolumn])
                    heapq.heappush(heap, GridPoint(nextrow, nextcolumn, next_max))

        return grid_heights[0][0]
