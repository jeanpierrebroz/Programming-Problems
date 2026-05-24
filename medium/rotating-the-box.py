class Solution:
    def rotateTheBox(self, boxGrid: List[List[str]]) -> List[List[str]]:
        n, m = len(boxGrid), len(boxGrid[0])
        rotated = [[None for _ in range(n)] for _ in range(m)]

        for i in range(n):
            for j in range(m):
                rotated[j][n - 1 -i] = boxGrid[i][j]


        for col in range(n):
            floor = m - 1
            for row in range(m - 1, -1, -1):
                if rotated[row][col] == "#":
                    rotated[row][col] = "."
                    rotated[floor][col] = "#"
                    floor -= 1
                elif rotated[row][col] == "*":
                    floor = row - 1
        return rotated