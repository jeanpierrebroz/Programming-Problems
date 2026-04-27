class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        graph = defaultdict(list)
        for source, target, time in times:
            graph[source].append((time, target))

        
        min_heap = [(0, k)]
        times = {}

        while min_heap:
            curr_cost, curr_node = heapq.heappop(min_heap)
            if curr_node in times and curr_cost > times[curr_node]:
                continue
            
            times[curr_node] = curr_cost

            for time, target in graph[curr_node]:

                if target not in times or time + curr_cost < times[target]:
                    times[target] = time + curr_cost
                    heapq.heappush(min_heap, (time + curr_cost, target))
        m = 0
        for i in range(1, n+1, 1):
            if i not in times:
                return -1
            m = max(m, times[i])
        
        return m
