class Solution:
    def numDecodings(self, s: str) -> int:
        # 1. Top-down strategy
        memo = {}

        def helper(index):
            if index == len(s):
                return 1
            if index > len(s):
                return 0
            
            if index in memo:
                return memo[index]
            
            ways = 0

            # choice 1: take single digit
            if s[index] != '0':
                ways += helper(index + 1)
            # choice 2: take two digits
            if index + 1 < len(s) and 10 <= int(s[index: index+2]) <= 26:
                ways += helper(index + 2)

            memo[index] = ways
            return ways

        return helper(0)
        