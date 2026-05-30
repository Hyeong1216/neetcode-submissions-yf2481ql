class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        # Questions:
        # 1. Is K always within range (0 <= k <= len(points))?
        # 2. what happens for the duplicate euclidean distance but different points?

        # Approaches:
        # 1. Brute force: create hashmap (k=[points pair], v=euclidean distance), sort the key and return kth largest element
        # 2. use heap? but no further idea

        # Answers:
        # Brute force
        points.sort(key=lambda p: p[0]**2 + p[1]**2)
        return points[:k]