class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        min_heap = [[math.sqrt(point[0]**2 + point[1]**2), point[0], point[1]] for point in points]
        heapq.heapify(min_heap)
        print(min_heap)
        
        res = []
        for _ in range(k):
            _, pointX, pointY = heapq.heappop(min_heap)
            res.append([pointX, pointY])

        return res