class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        max_heap = [-stone for stone in stones]
        heapq.heapify(max_heap)
        while len(max_heap) > 1:
            print(f"before popping two heaviest: {max_heap}")
            stone1 = -heapq.heappop(max_heap)
            stone2 = -heapq.heappop(max_heap)
            print(f"after popping two heaviest: {max_heap}")
            print(f"stone1:{stone1}||stone2:{stone2}")
            if stone1 > stone2:
                heapq.heappush(max_heap, (stone1-stone2) * -1)

            print(max_heap)
            print()

        return -max_heap[0] if max_heap else 0