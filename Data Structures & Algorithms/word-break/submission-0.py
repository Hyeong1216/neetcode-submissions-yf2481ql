class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        # 1. Top-down memoization: O(n ∗ m ∗ t)
        # Where n is the length of the string s, 
        # m is the number of words in wordDict and 
        # t is the maximum length of any word in wordDict.
        if not s and not wordDict:
            return True
        if not wordDict:
            return False
        
        memo = {}
        def helper(index):
            if index == len(s):
                return True
            
            if index in memo:
                return memo[index]
            
            for word in wordDict:
                if index + len(word) <= len(s) and s[index:index+len(word)] == word:
                    if helper(index + len(word)):
                        memo[index] = True
                        return True

            memo[index] = False
            return False
        return helper(0)