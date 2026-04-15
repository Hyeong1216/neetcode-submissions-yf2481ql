class Solution:
    def rob(self, nums: List[int]) -> int:
        # Space optimized
        rob = 0
        not_rob = 0

        # 두가지 선택지: rob, not_rob
        # rob > add num to the rob
        # not_rob > skip the num and not_rob should be previous best rob
        for num in nums:
            temp = rob
            rob = num + not_rob
            not_rob = max(temp, not_rob)



        return max(rob, not_rob)

        #--------------------------------------------------

        # 1. Bottom-up (use list)
        # if len(nums) == 1:
        #     return nums[0]

        # dp = [0] * len(nums)
        # dp[0] = nums[0]
        # dp[1] = max(nums[0], nums[1])

        # for i in range(2, len(nums)):
        #     dp[i] = max(nums[i] + dp[i-2], dp[i-1])

        # return dp[len(nums)-1]
        #--------------------------------------------------
        # 2. top-down memoization
        # memo = {}
        # def helper(i):
        #     if i >= len(nums):
        #         return 0
        #     if i == len(nums) - 1:
        #         return nums[i]
            
        #     if i in memo:
        #         return memo[i]
            
        #     rob_current = nums[i] + helper(i + 2)
        #     skip_current = helper(i + 1)

        #     result = max(rob_current, skip_current)

        #     memo[i] = result
        #     return result
        # return helper(0)
        #--------------------------------------------------
        # 3. space optimized
        rob = 0
        not_rob = 0

        for num in nums:
            temp = rob
            rob = num + not_rob
            not_rob = max(not_rob, temp)
        return max(rob, not_rob)
        
