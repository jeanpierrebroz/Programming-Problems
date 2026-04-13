class Solution:
    def getOrder(self, tasks: List[List[int]]) -> List[int]:
        class Task:
            def __init__(self, idx):
                self.idx = idx
            
            def __lt__(self, other):
                if tasks[self.idx][1] != tasks[other.idx][1]:
                    return tasks[self.idx][1] < tasks[other.idx][1]
                
                return self.idx < other.idx


        heap = []
        time = i = 0
        res = []
        
        n = len(tasks)
        indices = list(range(n))
        indices.sort(key= lambda i : (tasks[i][0], i))

        while heap or i < n:
            while i < n and tasks[indices[i]][0] <= time:
                heapq.heappush(heap, Task(indices[i]))
                i += 1
            
            if not heap:
                time = tasks[indices[i]][0]
            else:
                next_task = heapq.heappop(heap)
                time += tasks[next_task.idx][1]
                res.append(next_task.idx)

        return res
