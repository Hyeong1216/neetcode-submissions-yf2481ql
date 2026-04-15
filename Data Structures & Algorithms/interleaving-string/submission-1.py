class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        # bottom up
        if len(s1) + len(s2) != len(s3):
            return False
            
        dp = [[False] * (len(s2) + 1) for _ in range(len(s1) + 1)]
        dp[0][0] = True

        for i in range(1, len(s1) + 1):
            dp[i][0] = dp[i-1][0] and s1[i-1] == s3[i-1]
        
        for j in range(1, len(s2) + 1):
            dp[0][j] = dp[0][j-1] and s2[j-1] == s3[j-1]

        for i in range(1, len(s1) + 1):
            for j in range(1, len(s2) + 1):
                dp[i][j] = (dp[i-1][j] and s1[i-1] == s3[i+j-1]) or \
                (dp[i][j-1] and s2[j-1] == s3[i+j-1])

        return dp[len(s1)][len(s2)]










        #----------------------------------------------
        # top-down
        # memo = {}

        # def helper(s1_idx, s2_idx, s3_idx):
        #     if s3_idx == len(s3):
        #         return s1_idx == len(s1) and s2_idx == len(s2)
            
        #     if (s1_idx, s2_idx, s3_idx) in memo:
        #         return memo[(s1_idx, s2_idx, s3_idx)]

        #     result = False
        #     if s1_idx < len(s1) and s1[s1_idx] == s3[s3_idx]:
        #         result = result or helper(s1_idx+1, s2_idx, s3_idx+1)
        #     if s2_idx < len(s2) and s2[s2_idx] == s3[s3_idx]:
        #         result = result or helper(s1_idx, s2_idx+1, s3_idx+1)

        #     memo[(s1_idx, s2_idx, s3_idx)] = result
        #     return result

        # return helper(0, 0, 0)
