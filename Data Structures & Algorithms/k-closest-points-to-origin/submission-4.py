class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        # Questions
        # 1. Is k always within range (0 <= k <= len(points))?
        # 2. What happens for duplicate euclidean distance but different points?
        #    → return any k points (order doesn't matter)

        # Approach 1: Brute force (sort) — O(N log N)
        # points.sort(key=lambda p: p[0]**2 + p[1]**2)
        # return points[:k]

        # Approach 2: Max-heap size k — O(N log K)
        heap = []
        for x, y in points:
            dist = x**2 + y**2
            heapq.heappush(heap, (-dist, (x, y)))
            if len(heap) > k:
                heapq.heappop(heap)
        return [point for dist, point in heap]

        # Time: O(N log K), Space: O(K)
        # Why max-heap? Need to track and remove the FARTHEST point
        # Negate dist to simulate max-heap with Python's min-heap
        # vs Brute force: O(N log N) — heap wins when k << n