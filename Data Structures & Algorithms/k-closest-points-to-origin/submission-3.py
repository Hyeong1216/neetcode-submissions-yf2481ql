class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        # Questions
        # 1. Is k always within rangem (0 <= k <= len(points))?
        # 2. What happens for the duplicate euclidean distance but different points?

        # Answers
        # 1. Bruteforce
        # points.sort(key=lambda x: x[0]**2 + x[1]**2)
        # return points[:k]

        # 2. Heap
        heap = []
        for x, y in points:
            dist = x**2 + y**2
            heapq.heappush(heap, (-dist, (x, y)))
            if len(heap) > k:
                heapq.heappop(heap)
        return [point for dist, point in heap]









        #--------------------------------
        # Questions:
        # 1. Is K always within range (0 <= k <= len(points))?
        # 2. what happens for the duplicate euclidean distance but different points?

        # Approaches:
        # 1. Brute force: create hashmap (k=[points pair], v=euclidean distance), sort the key and return kth largest element
        # 2. use heap? but no further idea

        # Answers:
        # 1. Brute force
        # points.sort(key=lambda p: p[0]**2 + p[1]**2)
        # return points[:k]

        # 2. Heap
        # heap = []
        # for x, y in points:
        #     dist = x**2 + y**2
        #     heapq.heappush(heap, (-dist, (x, y)))
        #     if len(heap) > k:
        #         heapq.heappop(heap)
        # return [point for dist, point in heap]
        
# ## #973 Time Complexity

# ```
# n = len(points), k = k
# ```

# ### 현재 코드 (max-heap size k)
# ```
# heappush() × n번,  heap size는 최대 k+1
# 각 push/pop = O(log k)
# ─────────────────────────────
# Total: O(n log k)
# ```

# ### Brute force (sort)
# ```
# sort() = O(n log n)
# slicing = O(k)
# ─────────────────────────────
# Total: O(n log n)
# ```

# ---

# ## 왜 log k야?

# heap size가 항상 k로 유지되니까. heap에 원소가 k개 있을 때 push/pop 비용이 `log k`야.

# #215랑 완전히 같은 논리야:
# - 전체 n개 순회 → **n번**
# - 매번 heap 연산 → **log k**
# - 합치면 **O(n log k)**

# ---

# k가 n보다 훨씬 작을 때 (k=5, n=1,000,000) log k ≈ 2, log n ≈ 20 이니까 heap이 훨씬 빠른 거야.

# 다음 문제 갈까?