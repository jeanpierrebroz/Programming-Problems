class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:        
        rows, cols = len(heights), len(heights[0])
        visited_pacific = set()
        visited_atlantic = set()

        def dfs(row, col, visited, prevHeight):
            if ((row, col) in visited) or row < 0 or row >= rows or col < 0 or col >= cols or heights[row][col] < prevHeight:
                return
            
            visited.add((row, col))
            
            dfs(row + 1, col, visited, heights[row][col])
            dfs(row - 1, col, visited, heights[row][col])
            dfs(row, col + 1, visited, heights[row][col])
            dfs(row, col - 1, visited, heights[row][col])
        
        for c in range(cols):
            dfs(0, c, visited_pacific, heights[0][c])
            dfs(rows - 1, c, visited_atlantic, heights[rows-1][c])
        
        for r in range(rows):
            dfs(r, 0, visited_pacific, heights[r][0])
            dfs(r, cols-1, visited_atlantic, heights[r][cols-1])
        
        return list(visited_atlantic.intersection(visited_pacific))

            
