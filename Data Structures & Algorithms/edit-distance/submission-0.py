class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        # top down
        memo = {}
        def dp(i, j):
            if (i, j) in memo:
                return memo[(i, j)]

            # how many insert operations needed to make word1 same as word2
            if i == len(word1):
                return len(word2)-j
            
            # how many delete operations needed to make word1 same as word2
            if j == len(word2):
                return len(word1)-i
            
            result = 0
            if word1[i] == word2[j]:
                result =  dp(i+1, j+1)
            else:
                insert = 1 + dp(i, j+1)
                delete = 1 + dp(i+1, j)
                replace = 1 + dp(i+1, j+1)
                result = min(insert, delete, replace)
            memo[(i, j)] = result
            return result


        return dp(0, 0)