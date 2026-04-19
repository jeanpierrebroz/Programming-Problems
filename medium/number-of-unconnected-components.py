from collections import defaultdict
class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        visited = set()

        graph = defaultdict(list)

        for e1, e2 in edges:
            graph[e1].append(e2)
            graph[e2].append(e1)

        def dfs(n):
            if n in visited:
                return 
            visited.add(n)
            
            for neighbor in graph[n]:
                dfs(neighbor)
        
        l = len(visited)
        count = 0

        for i in range(n):
            if i not in visited:
                dfs(i)
                count += 1
        
        return count