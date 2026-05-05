class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:

        graph = defaultdict(list)
        for source, destination, price in flights:
            graph[source].append((destination, price))
        costs = {}
        for i in range(n):
            costs[i] = float('inf')
        
        def bfs(source, dest, k):
            q = deque()
            visited = set()
            q.append((source, 0))

            for _ in range(k + 2):
                for _ in range(len(q)):
                    currNode, prevCost = q.popleft()
                    costs[currNode] = min(costs[currNode], prevCost)
                    for neighbor, cost in graph[currNode]:
                        if costs[neighbor] > cost + prevCost:
                            q.append((neighbor, cost + prevCost))

                    
                k-=1
            return costs[dest] if costs[dest] != float('inf') else -1
        
        return bfs(src, dst, k)
