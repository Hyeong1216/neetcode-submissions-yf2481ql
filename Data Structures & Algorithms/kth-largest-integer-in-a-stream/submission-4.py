# 1. sorting
# class KthLargest:

#     def __init__(self, k: int, nums: List[int]):
#         self.k = k
#         self.arr = nums

#     def add(self, val: int) -> int:
#         self.arr.append(val)
#         self.arr.sort(reverse=True)
#         return self.arr[self.k-1]

# 2. min Heap
class KthLargest:
    def __init__(self, k: int, nums: List[int]):
        self.minHeap, self.k = nums, k
        heapq.heapify(self.minHeap)
        while len(self.minHeap) > self.k:
            heapq.heappop(self.minHeap)

    def add(self, val: int) -> int:
        heapq.heappush(self.minHeap, val)
        while len(self.minHeap) > self.k:
            heapq.heappop(self.minHeap)
        return self.minHeap[0]
        
