class Solution:
    def numDistinct(self, s: str, t: str) -> int:
        # Bottom up
        dp = [[0] * (len(t) + 1) for _ in range(len(s) + 1)]
        
        for i in range(len(s) + 1):
            dp[i][0] = 1
        
        for i in range(1, len(s) + 1):
            for j in range(1, len(t) + 1):
                dp[i][j] = dp[i-1][j]

                if s[i-1] == t[j-1]:
                    dp[i][j] += dp[i-1][j-1]

        return dp[len(s)][len(t)]
        











        #-----------------------------------------------
        # top down
        # memo = {}

        # def helper(s_idx, t_idx):
        #     if len(t) == t_idx:
        #         return 1
            
        #     if len(s) == s_idx:
        #         return 0

        #     if (s_idx, t_idx) in memo:
        #         return memo[(s_idx, t_idx)]
            
        #     result = 0
        #     if s[s_idx] == t[t_idx]:
        #         result += helper(s_idx+1, t_idx+1)
        #         result += helper(s_idx+1, t_idx)
        #     else:
        #         result += helper(s_idx+1, t_idx)

        #     memo[(s_idx, t_idx)] = result
        #     return result
        # return helper(0, 0)