class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        # 1. Top-down memoization: O(n ∗ m ∗ t)
        # Where n is the length of the string s, 
        # m is the number of words in wordDict and 
        # t is the maximum length of any word in wordDict.
        # if not s and not wordDict:
        #     return True
        # if not wordDict:
        #     return False
        
        # memo = {}
        # def helper(index):
        #     if index == len(s):
        #         return True
            
        #     if index in memo:
        #         return memo[index]
            
        #     for word in wordDict:
        #         if index + len(word) <= len(s) and s[index:index+len(word)] == word:
        #             if helper(index + len(word)):
        #                 memo[index] = True
        #                 return True

        #     memo[index] = False
        #     return False
        # return helper(0)
        #----------------------------------------------------------
        # 2. Bottom-up DP
        n = len(s)
        dp = [False] * (n+1)

        # Build solution from the end of string backwards to the beginning
        dp[n] = True # Base case: empty string can always be segmented

        # Fill DP array from end to beginning
        for i in range(n-1, -1, -1):
            for word in wordDict:
                if (i + len(word) <= n and
                    s[i:i+len(word)] == word and
                    dp[i + len(word)]):
                    dp[i] = True
                    break

        return dp[0]
