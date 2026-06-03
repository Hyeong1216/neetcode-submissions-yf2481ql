class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        # Questions
        # 1. Can the array have duplicate values?
        # 2. Is K always valid? (1 <= k <= nums.length?)
        # 3. can the array be empty?
        # 4. What's the expected size of the input?

        # Solution
        # 1. Sorting
        # nums.sort(reverse=True)
        # return nums[k-1]

        # 2. min-heap
        # heap = []
        # for num in nums:
        #     heapq.heappush(heap, num)
        #     if len(heap) > k:
        #         heapq.heappop(heap)
        # return heap[0]
        


        # 3. max-heap
        heap = [-num for num in nums]
        heapq.heapify(heap)
        for i in range(k-1):
            heapq.heappop(heap)
        return -heap[0]



















        #------------------------------------------------------------------
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
        # heap = [-num for num in nums]
        # heapq.heapify(heap)
        # for i in range(1, k):
        #     heapq.heappop(heap)
        # return -1 * heap[0]

# 결정적 차이
# n=1,000,000 / k=5 라고 하면:

# Max-heap: 100만개 전부 heap에 저장 → 메모리 100만
# Min-heap: 5개만 유지 → 메모리 5

# 시간도 Max-heap은 log n (n이 크면 클수록 느림), Min-heap은 log k (k가 작으면 엄청 빠름)

# Time complexity: "Both are valid, but min-heap is more efficient when k is much smaller than n — O(n log k) vs O(n + k log n)."












