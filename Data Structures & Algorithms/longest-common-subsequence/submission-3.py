class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        # 1. Recursive (Brute force): O(2^(m+n))
        # def helper(i, j):
        #     # i = current index in text1
        #     # j = current index in text2
        #     # returns: length of LCS between text1[i:] and text2[j:]
        #     if i == len(text1) or j == len(text2):
        #         return 0
            
        #     if text1[i] == text2[j]:
        #         return 1 + helper(i+1, j+1)
        #     else:
        #         choice1 = helper(i+1, j)
        #         choice2 = helper(i, j+1)
        #         return max(choice1, choice2)

        # return helper(0, 0)
        #-------------------------------------------------------------
        # 2. Top down:
        memo = {}
        def helper(i, j):
            if (i, j) in memo:
                return memo[(i, j)]

            if i == len(text1) or j == len(text2):
                return 0
            if text1[i] == text2[j]:
                result = 1 + helper(i+1, j+1)
            else:
                result = max(helper(i+1, j), helper(i, j+1))

            memo[(i, j)] = result
            return result

        return helper(0, 0)


        #-------------------------------------------------------------
        # 2. Bottom up

        # 3. 