class Solution:
    def checkIfPrerequisite(self, numCourses: int, prerequisites: List[List[int]], queries: List[List[int]]) -> List[bool]:
        #build a dag with prereq -> course 
        #do either dfs or bfs to figure out if prereq eventually leads to postreq
        #I'll use dfs 

        graph = defaultdict(list)
        result = [False for _ in range(len(queries))]
        for parent, child in prerequisites:
            graph[parent].append(child)

        i = 0
        for parent, child in queries:
           
            stk = [parent]
            visited = set()
            while stk:
                curr = stk.pop()
                if curr in visited:
                    continue
                for c in graph[curr]:
                    if c == child:
                        result[i] = True
                        continue
                    stk.append(c)
                    visited.add(curr)
            i += 1
            

        return result
