class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        #I wonder if there's a way to tell what the longest path something is a part of is once it's already been computed
        #like if I search 1, 2, 3, and 5, I should be able to "remember" what step of the path those steps are at, so if I encounter them as a valid step in the future I know immediately how much further they go without having to recalculate.

        #store path length in here
        cache = {}
        result = 0

        def getNeighbors(row: int, col: int):
            rows, cols = len(matrix), len(matrix[0])
            neighbors = []
            for dr, dc in ((1, 0), (-1, 0), (0, 1), (0, -1)):
                nr, nc = row + dr, col + dc
                if 0 <= nr < rows and 0 <= nc < cols:
                    neighbors.append((nr, nc))
            return neighbors

        def dfs(row, column):
            nonlocal cache

            if (row, column) in cache:
                return cache[(row, column)]

            neighbors = getNeighbors(row, column)
            
            m = 1
            for neighbor in neighbors:
                if matrix[neighbor[0]][neighbor[1]] > matrix[row][column]:
                    m = max(m, 1 + dfs(neighbor[0], neighbor[1]))
            
            cache[(row, column)] = m
            return m
        
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                result = max(result, dfs(i, j))
        
        return result