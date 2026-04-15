class Solution:
    def numDecodings(self, s: str) -> int:
        # 1. Top-down strategy
        # memo = {}

        # def helper(index):
        #     if index == len(s):
        #         return 1
        #     if index > len(s):
        #         return 0
            
        #     if index in memo:
        #         return memo[index]
            
        #     ways = 0

        #     # choice 1: take single digit
        #     if s[index] != '0':
        #         ways += helper(index + 1)
        #     # choice 2: take two digits
        #     if index + 1 < len(s) and 10 <= int(s[index: index+2]) <= 26:
        #         ways += helper(index + 2)

        #     memo[index] = ways
        #     return ways

        # return helper(0)

        # 2. Bottom up approach
        # n = len(s)
        # dp = [0] * (n+1)
        # dp[n] = 1
        
        # for i in range(n-1, -1, -1):
        #     ways = 0
        #     if s[i] != '0':
        #         ways += dp[i + 1]
        #     if i + 1 < n and 10 <= int(s[i:i+2]) <= 26:
        #         ways += dp[i + 2]
        #     dp[i] = ways
        # return dp[0]

        # 3. Space optimized DP
        if not s or s[0] == '0':
            return 0
        
        # these represent dp[i+2] and dp[i+1] as we iterate backwards
        prev2 = 1
        prev1 = 1 if s[-1] != '0' else 0

        for i in range(len(s) -2, -1, -1):
            current = 0

            if s[i] != '0':
                current += prev1
            if i + 1 < len(s) and 10 <= int(s[i:i+2]) <= 26:
                current += prev2
            prev2 = prev1
            prev1 = current
        return prev1