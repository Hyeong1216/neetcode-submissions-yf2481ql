class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        # Recursion
        # def dfs(i):
        #     if i >= len(cost):
        #         return 0
        #     return cost[i] + min(dfs(i+1), dfs(i+2))

        # return min(dfs(0), dfs(1))
        #---------------------------------------------
        # Top-down
        memo = [-1] * len(cost)

        def dfs(i):
            if i >= len(cost):
                return 0
            if memo[i] != -1:
                return memo[i]            

            memo[i] = cost[i] + min(dfs(i+1), dfs(i+2))

            return memo[i]

        return min(dfs(0), dfs(1))

        #---------------------------------------------
        # bottom-up 
        # (dp[i] represents the minimum cost to reath the ith step)
        # n = len(cost)
        # dp = [0] * (n + 1)

        # for i in range(2, n+1):
        #     dp[i] = min((dp[i-1] + cost[i-1]), (dp[i-2] + cost[i-2]))

        # return dp[n]
        #---------------------------------------------
        # # DP space optimized
        # for i in range(len(cost) - 3, -1, -1):
        #     cost[i] += min(cost[i+1], cost[i+2])
        # return min(cost[0], cost[1])
        
