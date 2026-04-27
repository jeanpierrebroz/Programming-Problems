class Solution:
    def shortestPath(self, n: int, edges: List[List[int]], src: int) -> Dict[int, int]:
        graph = defaultdict(list)

        for source, dest, weight in edges:
            graph[source].append((weight, dest))

        min_heap = [(0, src)]

        costs = {src: 0}

        while min_heap:
            curr_cost, curr_node = heapq.heappop(min_heap)

            if curr_cost > costs.get(curr_node, float("inf")):
                continue
            
            for weight, dest in graph[curr_node]:
                if dest not in costs or costs[dest] > curr_cost + weight:
                    costs[dest] = weight + curr_cost
                    heapq.heappush(min_heap, (weight + curr_cost, dest))
        
        result = {i: costs.get(i, -1) for i in range(n)}
        return result