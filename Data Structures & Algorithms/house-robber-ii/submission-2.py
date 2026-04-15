class Solution:
    def rob(self, nums: List[int]) -> int:
        # 1. Bottom-up (use list)
        # if len(nums) == 1:
        #     return nums[0]
        # if len(nums) == 2:
        #     return max(nums[0], nums[1])

        # scenario1_houses = nums[:-1]
        # scenario2_houses = nums[1:]

        # def rob_linear(houses):
        #     if len(houses) == 1:
        #         return houses[0]
        #     dp = [0] * len(houses)
        #     dp[0] = houses[0]
        #     dp[1] = max(houses[0], houses[1])
        #     for i in range(2, len(houses)):
        #         dp[i] = max(houses[i] + dp[i-2], dp[i-1])
        #     return dp[len(houses)-1]


        # scenario1_result = rob_linear(scenario1_houses)
        # scenario2_result = rob_linear(scenario2_houses)
        
        # return max(scenario1_result, scenario2_result)

        # 2. top-down memoization
        if len(nums) == 1:
            return nums[0]
        if len(nums) == 2:
            return max(nums[0], nums[1])
        
        scenario1_houses = nums[:-1]
        scenario2_houses = nums[1:]

        def rob_linear_recursive(houses):
            memo = {}
            def helper(i):
                if i >= len(houses): # out of bounds
                    return 0
                if i == len(houses) - 1: # last house
                    return houses[i]

                if i in memo:
                    return memo[i]
                
                rob_current = houses[i] + helper(i + 2)
                skip_current = helper(i + 1)

                result = max(rob_current, skip_current)

                memo[i] = result
                return result
            return helper(0)
        

        scenario1_result = rob_linear_recursive(scenario1_houses)
        scenario2_result = rob_linear_recursive(scenario2_houses)

        return max(scenario1_result, scenario2_result)


        # 3. space optimized
        # rob = 0
        # not_rob = 0

        # for num in nums:
        #     temp = rob
        #     rob = num + not_rob
        #     not_rob = max(not_rob, temp)
        # return max(rob, not_rob)
        
