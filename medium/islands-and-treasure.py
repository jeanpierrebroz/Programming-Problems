class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        visited = set()
        q = deque()
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 0:
                    q.append((i, j))

        steps = 0
        while q:
            for _ in range(len(q)):
                i, j = q.popleft()
                visited.add((i, j))

                if grid[i][j] == -1:
                    continue

                if grid[i][j] > 1:
                    grid[i][j] = min(grid[i][j], steps)

                dirs = [(1, 0), (0, 1), (-1, 0), (0, -1)]

                for d in dirs:
                    ni, nj = i + d[0], j + d[1]
                    if 0 <= ni < len(grid) and 0 <= nj < len(grid[0]):
                        if (ni, nj) not in visited and grid[ni][nj] > 0:
                            q.append((ni, nj))
            steps += 1

        return                