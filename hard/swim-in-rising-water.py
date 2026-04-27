class Solution:
    def swimInWater(self, grid: List[List[int]]) -> int:
        #(cost, row, col)
        min_heap = [(grid[0][0], 0, 0)]

        def getValidNeighbors(row, col):
            directions = [(1, 0), (0, 1), (-1, 0), (0, -1)]
            neighbors = []
            for d in directions:
                newRow, newCol = row + d[0], col + d[1]
                if 0 <= newRow < len(grid) and 0 <= newCol < len(grid):
                    neighbors.append((grid[newRow][newCol], newRow, newCol))
            
            return neighbors

        visited = set() 

        while min_heap:
            cost, row, col = heapq.heappop(min_heap)
            if row == col == len(grid) - 1:
                return cost

            neighbors = getValidNeighbors(row, col)

            for neighbor in neighbors:
          
                if (neighbor[1], neighbor[2]) not in visited:
                    visited.add((neighbor[1], neighbor[2]))
                    heapq.heappush(min_heap, (max(neighbor[0], cost), neighbor[1], neighbor[2]))
        
        return grid[0][0]