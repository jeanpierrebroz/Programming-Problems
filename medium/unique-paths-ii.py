class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        #same grid approach as before, but grid[i][j] must be 0 if i, j is the coordinate of an obstacle. as well as all paths it "blocks" for base case
        m, n = len(obstacleGrid), len(obstacleGrid[0])
        if obstacleGrid[0][0] == 1:
            return 0
        if m == 1 or n == 1:
            return 1

        grid = [[0 for _ in range(n)] for _ in range(m)]

        flag = False
        for i in range(1, m):
            if obstacleGrid[i][0] == 1:
                flag = True
            grid[i][0] = 0 if flag else 1

        flag = False
        for i in range(1, n):
            if obstacleGrid[0][i] == 1:
                flag = True
            grid[0][i] = 0 if flag else 1

        
        
        for i in range(1, m):
            for j in range(1, n):
                if obstacleGrid[i][j] != 1:
                    grid[i][j] = grid[i-1][j] + grid[i][j-1]

        return grid[m-1][n-1]