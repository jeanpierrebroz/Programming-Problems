class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        if len(edges) != n - 1:
            return False
        graph = defaultdict(list)
        for src, dest in edges:
            if dest == src:
                return False
            graph[src].append(dest)
            graph[dest].append(src)
        
        visited = set()
        def dfs(node, parent):
            visited.add(node)

            for neighbor in graph[node]:
                if neighbor == parent:
                    continue
                if neighbor in visited:
                    continue
                dfs(neighbor, node)                    
            
        dfs(0, -1)
        return len(visited) == n
