class MedianFinder:

    def __init__(self):
        # use two heaps: minheap and maxheap
        self.small = [] #maxHeap
        self.large = [] #minHeap

    def addNum(self, num: int) -> None:
        #1. if/else 
        #if (self.large not None AND num > self.large[0]) > heappush(large, num)
        #else (heappush(small, -1 * num)) to implement maxHeap in python
        #2. two ifs that move value if length of two heaps diffs more than 2
        if self.large and num > self.large[0]:
            heapq.heappush(self.large, num)
        else:
            heapq.heappush(self.small, -1 * num)
        if len(self.small) > len(self.large) + 1:
            val = -1 * heapq.heappop(self.small)
            heapq.heappush(self.large, val)
        if len(self.small) + 1 < len(self.large):
            val = heapq.heappop(self.large)
            heapq.heappush(self.small, -1 * val)

    def findMedian(self) -> float:
        # len of small is greater or large greateer, return correspondingly
        # if lengths are same, then compute and return
        if len(self.small) > len(self.large):
            return -1 * self.small[0]
        elif len(self.small) < len(self.large):
            return self.large[0]
        return ((-1 * self.small[0]) + self.large[0]) / 2.0
        