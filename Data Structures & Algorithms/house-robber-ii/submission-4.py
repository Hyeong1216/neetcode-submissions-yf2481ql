class Solution:
    def rob(self, nums: List[int]) -> int:
        # 1. Bottom-up 
        if len(nums) == 1:
            return nums[0]
        if len(nums) == 2:
            return max(nums[1], nums[0])
        
        scenario1 = nums[1:]
        scenario2 = nums[:-1]
        def helper(house):
            dp = [0] * len(house)
            dp[0] = house[0]
            dp[1] = max(house[0], house[1])

            for i in range(2, len(house)):
                dp[i] = max(house[i] + dp[i-2], dp[i-1])
            return dp[len(house)-1]

        
        result1 = helper(scenario1)
        result2 = helper(scenario2)

        return max(result1, result2)





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
        # if len(nums) == 1:
        #     return nums[0]
        # if len(nums) == 2:
        #     return max(nums[0], nums[1])
        
        # scenario1_houses = nums[:-1]
        # scenario2_houses = nums[1:]

        # def rob_linear_recursive(houses):
        #     memo = {}
        #     def helper(i):
        #         if i >= len(houses): # out of bounds
        #             return 0
        #         if i == len(houses) - 1: # last house
        #             return houses[i]

        #         if i in memo:
        #             return memo[i]
                
        #         rob_current = houses[i] + helper(i + 2)
        #         skip_current = helper(i + 1)

        #         result = max(rob_current, skip_current)

        #         memo[i] = result
        #         return result
        #     return helper(0)
        

        # scenario1_result = rob_linear_recursive(scenario1_houses)
        # scenario2_result = rob_linear_recursive(scenario2_houses)

        # return max(scenario1_result, scenario2_result)


        # 3. space optimized
        if len(nums) == 1:
            return nums[0]
        if len(nums) == 2:
            return max(nums[0], nums[1])

        def rob_linear_optimized(houses):
            rob = 0
            not_rob = 0

            for num in houses:
                temp = rob
                rob = num + not_rob
                not_rob = max(not_rob, temp)
            return max(rob, not_rob)
            
        scenario1_result = rob_linear_optimized(nums[:-1])
        scenario2_result = rob_linear_optimized(nums[1:])

        return max(scenario1_result, scenario2_result)

        
