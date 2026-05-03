class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        #tickets[i] = [source, dest]
        #source and dest are 3 uppercase english letters
        #reconstruct itinerary in order and return
        #each ticket was used EXACTLY ONCE
        #if there are multiple flight paths, return lexicographically smallest one
        #
        #always start at jfk
        SOURCE_NODE = "JFK"
        #explore paths from jfk 
        #jfk -> abc -> jfk -> xyz -> jfk -> zzz


        graph = defaultdict(list)
        taken = defaultdict(int)
        for source, dest in tickets:
            graph[source].append(dest)
            taken[(source, dest)] += 1
        
        for key in graph.keys():
            graph[key].sort()

        def dfs(curr_node, path, taken):
            print(path, taken, curr_node)
            if len(path) == len(tickets) + 1:
                return path
            

            for neighbor in graph[curr_node]:
                if taken[(curr_node, neighbor)] == 0:
                    continue
                taken[(curr_node, neighbor)] -= 1
                path.append(neighbor)

                if dfs(neighbor, path, taken):
                    return path
                path.pop()
                taken[(curr_node, neighbor)] += 1
                  
            return []

        return dfs(SOURCE_NODE, [SOURCE_NODE], taken)


            

