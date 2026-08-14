class Solution:
    def rob(self, nums: List[int]) -> int:
        # Bottom up
        if len(nums) == 1:
            return nums[0]
        
        dp = [0] * len(nums)
        dp[0] = nums[0] 
        dp[1] = max(nums[0], nums[1])

        for i in range(2, len(nums)):
            dp[i] = max((nums[i] + dp[i-2]), (dp[i-1]))
        return dp[len(nums)-1]




        # 2. top-down memoization

        # max amount of if I skip this house
        # in each round we have two choices, either rob or not rob
        # compute each choices and go with higher yield\
        # if len(nums) < 1:
        #     return nums[0]
        # if len(nums) < 2:
        #     return max(nums[0], nums[1])
        # memo = {}
        # memo[0] = nums[0] 
        # memo[1] = max(nums[0], nums[1])
        # for i in range(2, len(nums)):

        #     if i in memo:
        #         return memo[i]

        #     memo[i] = max((nums[i] + memo[i-2]), (memo[i-1]))
        
        # print(memo)
        # return memo[len(nums)-1]

            























# class Solution:
#     def rob(self, nums: List[int]) -> int:
#         # Questions:
#         # 1. Can len(nums) be zero?

#         # Key insight: at each house, choose max of:
#         # - skip current: dp[i-1]
#         # - rob current: dp[i-2] + nums[i]

#         # Approach 1: Bottom-up DP — O(N) time, O(N) space
#         if len(nums) == 1:
#             return nums[0]
#         dp = [0] * len(nums)
#         dp[0] = nums[0]
#         dp[1] = max(nums[0], nums[1])
#         for i in range(2, len(nums)):
#             dp[i] = max(dp[i-1], dp[i-2] + nums[i])
#         return dp[-1]

#         # Approach 2: Top-down memoization — O(N) time, O(N) space
#         # memo = {}
#         # def helper(i):
#         #     if i >= len(nums): return 0
#         #     if i in memo: return memo[i]
#         #     memo[i] = max(nums[i] + helper(i+2), helper(i+1))
#         #     return memo[i]
#         # return helper(0)

#         # Approach 3: Space-optimized — O(N) time, O(1) space
#         # prev2, prev1 = 0, 0
#         # for num in nums:
#         #     temp = max(prev1, prev2 + num)
#         #     prev2 = prev1
#         #     prev1 = temp
#         # return prev1

#         # Time: O(N), Space: O(N) bottom-up / O(1) space-optimized