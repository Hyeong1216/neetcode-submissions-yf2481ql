import heapq
from collections import Counter
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq_map = Counter(nums)
        minHeap = []

        for key, value in freq_map.items():
            heapq.heappush(minHeap, (value, key))
            print("length: ", len(minHeap))
            if len(minHeap) > k:
                heapq.heappop(minHeap)
        return [num for freq, num in minHeap]
