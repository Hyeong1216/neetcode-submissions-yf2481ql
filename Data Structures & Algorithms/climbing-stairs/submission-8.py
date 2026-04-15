class Solution:
    def climbStairs(self, n: int) -> int:
        # 1. Recursive with memoization (top-down)
        # memo = {}
        # def helper(step):
        #     if step in memo:
        #         return memo[step]
            
        #     if step == 1:
        #         return 1
        #     if step == 2:
        #         return 2

        #     memo[step] = helper(step-1) + helper(step-2)
        #     return memo[step]
        # return helper(n)

        memo = {}
        def helper(step):
            if step in memo:
                return memo[step]
            if step == 1:
                return 1
            if step == 2:
                return 2
            memo[step] = helper(step-1) + helper(step-2)
            return memo[step]
        return helper(n)

        # 2. Iterative DP (bottom-up)
        # if n <= 2:
        #     return n
        # dp = [0] * (n + 1)

        # dp[1] = 1
        # dp[2] = 2
        # for i in range(3, n + 1):
        #     dp[i] = dp[i-1] + dp[i-2]
        # return dp[n]



        # 3. Space-optimized (just track last 2 values)
        # if n <= 3:
        #     return n
        # n1, n2 = 2, 3
        # for i in range(4, n + 1):
        #     temp = n1 + n2
        #     n1 = n2
        #     n2 = temp
        # return n2
        
