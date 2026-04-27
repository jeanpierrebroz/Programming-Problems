class Solution:
    def maxProbability(self, n: int, edges: List[List[int]], succProb: List[float], start_node: int, end_node: int) -> float:
        #we should be able to use dijkstra's for this (along with a visited set to ensure no inf loop)

        visited = set()

        graph = defaultdict(list)

        for i, edge in enumerate(edges):
            graph[edge[0]].append((succProb[i], edge[1]))
            graph[edge[1]].append((succProb[i], edge[0]))

        
        max_heap = [(1.0, start_node)]
        heapq.heapify_max(max_heap)

        while max_heap:
            
            curr_prob, curr_node = heapq.heappop_max(max_heap)
            visited.add(curr_node)

            if curr_node == end_node:
                return curr_prob
            
            for prob, node in graph[curr_node]:
                if node not in visited:
                    new_prob = curr_prob * prob
                    heapq.heappush_max(max_heap, (new_prob, node))
        
        return 0