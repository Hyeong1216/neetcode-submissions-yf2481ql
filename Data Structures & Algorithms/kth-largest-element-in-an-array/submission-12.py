class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        # heap - best
        heap = []
        for num in nums:
            heapq.heappush(heap, num)
            if len(heap) > k:
                heapq.heappop(heap)
        return heap[0]




        #-----------------------------------------------------
        # heap - naive ans
        # heapq.heapify(nums)
        # return heapq.nlargest(k, nums)[k-1]
        #-----------------------------------------------------
        # sorting bruteforce
        # nums.sort(reverse=True)
        # return nums[k-1]


































# class Solution:
#     def findKthLargest(self, nums: List[int], k: int) -> int:
#         # Questions
#         # 1. Can the array have duplicate values?
#         # 2. Is K always valid? (1 <= k <= nums.length?)
#         # 3. Can the array be empty?
#         # 4. What's the expected size of the input?

#         # Approach 1: Sorting — O(N log N)
#         # nums.sort(reverse=True)
#         # return nums[k-1]

#         # Approach 2: Min-heap — O(N log K)
#         # heap = []
#         # for num in nums:
#         #     heapq.heappush(heap, num)
#         #     if len(heap) > k:
#         #         heapq.heappop(heap)
#         # return heap[0]

#         # Approach 3: Max-heap — O(N + K log N)
#         # heap = [-num for num in nums]
#         # heapq.heapify(heap)
#         # for i in range(k-1):
#         #     heapq.heappop(heap)
#         # return -heap[0]

#         # Best: Min-heap (optimal when k << n)
#         heap = []
#         for num in nums:
#             heapq.heappush(heap, num)
#             if len(heap) > k:
#                 heapq.heappop(heap)
#         return heap[0]

#         # Time: O(N log K), Space: O(K)
#         # vs Max-heap: O(N + K log N), Space: O(N)
#         # Min-heap wins when k << n (e.g. k=5, n=1,000,000)