class Solution:
    def climbStairs(self, n: int) -> int:
        # 1. top down - memoization
        memo = {}
        def helper(step):
            if step in memo:
                return memo[step]
            if step == 1:
                return 1
            if step == 2:
                return 2
            memo[step] = helper(step - 1) + helper(step - 2)
            return memo[step]

        

        return helper(n)



        # 2. bottom up























# class Solution:
#     def climbStairs(self, n: int) -> int:


#         # Questions:
#         # 1. Can n be zero?

#         # Key insight: dp[i] = dp[i-1] + dp[i-2] (Fibonacci pattern)
#         # To reach step i, you came from i-1 (1 step) or i-2 (2 steps)

#         # Approach 1: Top-down memoization — O(N) time, O(N) space
#         # memo = {}
#         # def helper(step):
#         #     if step in memo: return memo[step]
#         #     if step == 1: return 1
#         #     if step == 2: return 2
#         #     memo[step] = helper(step-1) + helper(step-2)
#         #     return memo[step]
#         # return helper(n)

#         # Approach 2: Bottom-up DP — O(N) time, O(N) space
#         # if n <= 2: return n
#         # dp = [0] * (n + 1)
#         # dp[1] = 1
#         # dp[2] = 2
#         # for i in range(3, n+1):
#         #     dp[i] = dp[i-1] + dp[i-2]
#         # return dp[n]

#         # Approach 3: Space-optimized — O(N) time, O(1) space
#         if n <= 2:
#             return n
#         n1, n2 = 1, 2
#         for i in range(3, n+1):
#             temp = n1 + n2
#             n1 = n2
#             n2 = temp
#         return n2

#         # Time: O(N), Space: O(1) — only track last 2 values