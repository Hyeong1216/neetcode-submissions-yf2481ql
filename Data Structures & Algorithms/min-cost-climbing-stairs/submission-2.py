class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        # bottom-up 
        # (dp[i] represents the minimum cost to reath the ith step)
        n = len(cost)
        dp = [0] * (n + 1)

        for i in range(2, n+1):
            dp[i] = min((dp[i-1] + cost[i-1]), (dp[i-2] + cost[i-2]))

        return dp[n]