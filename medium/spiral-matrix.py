class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        result = []
        n, m = len(matrix), len(matrix[0])
        rows, cols = 0, 0

        
        while len(result) < m * n:
            #top row
            #side
            #bottom
            #up
            #incr rows and cols
            for i in range(cols, m - cols):
                if len(result) < n * m: result.append(matrix[rows][i])
            
            for i in range(rows + 1, n - rows):
                if len(result) < n * m: result.append(matrix[i][m - cols - 1])
            
            for i in range(m - cols - 2, cols - 1, -1):
                if len(result) < n * m: result.append(matrix[n - rows - 1][i])
            
            for i in range(n - rows - 2, rows, -1):
                if len(result) < n * m: result.append(matrix[i][cols])
            
            rows += 1
            cols += 1
        
        return result