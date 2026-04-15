class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        # Bottom up
        m, n = len(word1), len(word2)
        dp = [[0]*(n+1) for _ in range(m+1)]

        # dp[i][j] = min operations to convert word1[0:i] to word2[0:j]

        # dp[0][j] = converting empty string to word2[0:j]
        for j in range(n+1):
            dp[0][j] = j

        # dp[i][0] = converting word1[0:i] to empty string
        for i in range(m+1):
            dp[i][0] = i
        
        for i in range(1, m+1):
            for j in range(1, n+1):
                # TODO: Fill in the logic here
                # Hint: It's very similar to your top-down approach!
                # But remember: dp[i][j] corresponds to word1[i-1] and word2[j-1]
                # (because of the extra row/column for empty strings)
                if word1[i-1] == word2[j-1]:
                    dp[i][j] = dp[i-1][j-1]
                else:
                    insert = 1 + dp[i][j-1]
                    delete = 1 + dp[i-1][j]
                    replace = 1 + dp[i-1][j-1]
                    dp[i][j] = min(insert, delete, replace) #three cases here
        return dp[m][n]

        #------------------------------------------------------------
        # top down
        # memo = {}
        # def dp(i, j):
        #     if (i, j) in memo:
        #         return memo[(i, j)]

        #     # how many insert operations needed to make word1 same as word2
        #     if i == len(word1):
        #         return len(word2)-j
            
        #     # how many delete operations needed to make word1 same as word2
        #     if j == len(word2):
        #         return len(word1)-i
            
        #     result = 0
        #     if word1[i] == word2[j]:
        #         result =  dp(i+1, j+1)
        #     else:
        #         insert = 1 + dp(i, j+1) # i stays the same (we haven't processed word1[i] yet, we just inserted before it)
        #         delete = 1 + dp(i+1, j) # insert의 경우 i전에 넣으면 현제 i에 있던 char은 밀리게 되어 다음 i+1로 넘어간다, 그래서 i stays the same, delete의 경우 반대
        #         replace = 1 + dp(i+1, j+1)
        #         result = min(insert, delete, replace)
        #     memo[(i, j)] = result
        #     return result

        # return dp(0, 0)