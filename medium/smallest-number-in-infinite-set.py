import heapq

class SmallestInfiniteSet:
    def __init__(self):
        self.added_back = [] 
        self.in_heap = set()
        self.next_val = 1   

    def popSmallest(self) -> int:
        if self.added_back:
            smallest = heapq.heappop(self.added_back)
            self.in_heap.remove(smallest)
            return smallest
        res = self.next_val
        self.next_val += 1
        return res

    def addBack(self, num: int) -> None:
        if num < self.next_val and num not in self.in_heap:
            heapq.heappush(self.added_back, num)
            self.in_heap.add(num)
