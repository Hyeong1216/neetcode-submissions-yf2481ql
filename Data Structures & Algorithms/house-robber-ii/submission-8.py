class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]
        if len(nums) == 2:
            return max(nums[0], nums[1])
        
        scenario1 = nums[:-1]
        scenario2 = nums[1:]

        def rob(houses):
            dp = [0] * len(houses)
            dp[0] = houses[0]
            dp[1] = max(houses[0], houses[1])
            for i in range(2, len(houses)):
                rob = dp[i-2] + houses[i]
                not_rob = dp[i-1]
                dp[i] = max(rob, not_rob)
            
            return dp[len(houses)-1]


        

        return(max(rob(scenario1), rob(scenario2)))


        