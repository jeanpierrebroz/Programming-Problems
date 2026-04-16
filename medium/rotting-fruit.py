from collections import deque
class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        #make initial pass thru grid to find coords of all rotten fruits
        seen = set()
        minutes = -1
        fruit_count = 0

        #find our rotten fruit
        q = deque()

        for i in range(len(grid)):
            for j, space in enumerate(grid[i]):
                if space == 2:
                    q.append((i, j))
                    fruit_count+=1
                elif space == 1:
                    fruit_count+=1
        
        
        def getNeighbors(pos):
            nb = []
            if pos[0] > 0:
                nb.append((pos[0]-1, pos[1]))
            if pos[1] > 0:
                nb.append((pos[0], pos[1]-1))
            if pos[0] < len(grid) - 1:
                nb.append((pos[0] + 1, pos[1]))
            if pos[1] < len(grid[0])-1:
                nb.append((pos[0], pos[1] + 1))
            return nb
        
        while q:
            for _ in range(len(q)):
                curr_position = q.popleft()
                seen.add(curr_position)
                fruit_count -= 1
                neighbors = getNeighbors(curr_position)
                for n in neighbors:

                    if grid[n[0]][n[1]] == 1:
                        grid[n[0]][n[1]] = 2

        
                    
                        if n not in seen:
                            q.append(n)
                    
                    seen.add(n)

            minutes+=1

        if fruit_count > 0:
            return -1
        
        return max(0, minutes)