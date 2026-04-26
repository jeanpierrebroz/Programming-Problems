class Solution:
    def findMaximizedCapital(self, k: int, w: int, profits: List[int], capital: List[int]) -> int:

        projects = [(capital_required, profit) for capital_required, profit in zip(capital, profits)]
        projects.sort()
        profs = []
        curr = 0
        for _ in range(k):
            
            while curr < len(projects) and projects[curr][0] <= w:
                heapq.heappush_max(profs, projects[curr][1])
                curr+=1
            
            if not profs:
                break
            
            w += heapq.heappop_max(profs)

        return w