class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        # sliding window
        # res = []
        # for i in range(len(nums)-k+1):
        #     res.append(max(nums[i:i+k]))
        # return res
        #=--------------------------------------------------------
        dq = deque()
        result = []

        for i in range(len(nums)):
            # step 1: remove indices outside current window
            while dq and dq[0] <= i - k:
                dq.popleft()

            # step 2: maintain decreasing oreder (remove smaller elements)
            while dq and nums[dq[-1]] <= nums[i]:
                dq.pop()

            # step 3: Add current index
            dq.append(i)
            
            # step 4: record result when window is full
            if i >= k - 1:
                result.append(nums[dq[0]])
        return result
