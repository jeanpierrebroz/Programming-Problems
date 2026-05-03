class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        SOURCE_NODE = "JFK"

        graph = defaultdict(list)
        for source, dest in sorted(tickets)[::-1]:
            graph[source].append(dest)
        
        result = []
        def dfs(curr_node):
            while graph[curr_node]:
                neighbor = graph[curr_node].pop()
                dfs(neighbor)
            result.append(curr_node)

        dfs(SOURCE_NODE)
        return result[::-1]