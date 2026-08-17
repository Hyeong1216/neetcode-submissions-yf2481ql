class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        # 3. Bottom up
        m, n = len(text1), len(text2)
        dp = [[0] * (n + 1) for _ in range(m + 1)]
        for i in range(1, m+1):
            for j in range(1, n+1):
                if text1[i-1] == text2[j-1]:
                    dp[i][j] = 1 + dp[i-1][j-1]
                else:
                    dp[i][j] = max(dp[i-1][j], dp[i][j-1])


        return dp[m][n]



# class Solution:
#     def longestCommonSubsequence(self, text1: str, text2: str) -> int:
#         # 2. Top down
#         memo = {}
#         def helper(i, j):
#             if (i, j) in memo:
#                 return memo[(i, j)]
#             if i == len(text1) or j == len(text2):
#                 return 0
            
#             curr_res = 0

#             if text1[i] == text2[j]:
#                 curr_res = 1 + (helper(i + 1, j + 1))
#             else:
#                 curr_res = max(helper(i + 1, j), helper(i, j + 1))
            
#             memo[(i, j)] = curr_res
#             return curr_res

#         return helper(0, 0)








# class Solution:
#     def longestCommonSubsequence(self, text1: str, text2: str) -> int:
#         # 1. Brute force
#         def helper(i, j):
#             if i == len(text1) or j == len(text2):
#                 return 0

#             if text1[i] == text2[j]:
#                 return 1 + helper(i + 1, j + 1)
#             else:
#                 return max(helper(i + 1, j), helper(i, j+1))
#         return helper(0, 0)