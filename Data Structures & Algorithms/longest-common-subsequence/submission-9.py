class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        # 2. Top down
        memo = {}
        def helper(i, j):
            if (i, j) in memo:
                return memo[(i, j)]
            if i == len(text1) or j == len(text2):
                return 0
            
            curr_res = 0

            if text1[i] == text2[j]:
                curr_res = 1 + (helper(i + 1, j + 1))
                
            else:
                curr_res = max(helper(i + 1, j), helper(i, j + 1))
            
            memo[(i, j)] = curr_res
            return curr_res

        return helper(0, 0)








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