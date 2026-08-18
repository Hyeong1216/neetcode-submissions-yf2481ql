# class Solution:
#     def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
#         res = []
#         for i in range(len(nums)-k+1):
#             res.append(max(nums[i:i+k]))
#         return res

#--------------------------------------------------
class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        # Questions
        # 1. Can k be 0?
        # 2. can nums be empty list?
        
        # Soltion (monotonic deque)
        res = []
        q = deque()
        for i in range(len(nums)):
            while q and q[0] <= i - k:
                q.popleft()
            
            while q and nums[q[-1]] < nums[i]:
                q.pop()
            q.append(i)
            if i >= k-1:
                res.append(nums[q[0]])
            # print(q)
            
        return res












