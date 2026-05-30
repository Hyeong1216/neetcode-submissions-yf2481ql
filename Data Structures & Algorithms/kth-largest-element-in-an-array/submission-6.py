class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        # Questions:
        # *1. Can the array have duplicate values?
        # 2. Is k always valid? (1 <= k <= nums.length?)
        # 3. Can the array be empty?
        # *4. What's the expected size of the input?

        # Answers:
        # 1. Bruteforce
        # nums.sort(reverse=True)
        # print(nums)
        # for i in range(len(nums)):
        #     if i == k-1:
        #         return nums[i]
        
        # 2. Min-heap
        # heap = []
        # for num in nums:
        #     heapq.heappush(heap, num)
        #     if len(heap) > k:
        #         heapq.heappop(heap)
        # return heap[0]

        # 3. Max-heap
        heap = [-num for num in nums]
        heapq.heapify(heap)
        for i in range(1, k):
            heapq.heappop(heap)
        return -1 * heap[0]














