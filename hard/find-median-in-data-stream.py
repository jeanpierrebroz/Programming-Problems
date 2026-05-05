class MedianFinder:

    def __init__(self):
        self.min_heap = []
        self.max_heap = []

    def addNum(self, num: int) -> None:

        heapq.heappush_max(self.max_heap, num)

        if self.max_heap and self.min_heap and self.max_heap[0] > self.min_heap[0]:
            heapq.heappush(self.min_heap, heapq.heappop_max(self.max_heap))

        if len(self.max_heap) > len(self.min_heap) + 1:
            heapq.heappush(self.min_heap, heapq.heappop_max(self.max_heap))
        elif len(self.min_heap) > len(self.max_heap):
            heapq.heappush_max(self.max_heap, heapq.heappop(self.min_heap))

    def findMedian(self) -> float:
        if (len(self.min_heap) + len(self.max_heap)) % 2 == 0:
            return (self.min_heap[0] + self.max_heap[0]) / 2.0
        return float(self.max_heap[0])