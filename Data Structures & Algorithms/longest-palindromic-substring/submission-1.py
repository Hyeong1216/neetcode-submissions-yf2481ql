class Solution:
    def longestPalindrome(self, s: str) -> str:
        # 1. brute force
        def is_palindfrome(substring):
            l, r = 0, len(substring) - 1
            while l < r:
                if substring[l] != substring[r]:
                    return False
                l += 1
                r -= 1
            return True

        longest = ""

        for i in range(len(s)):
            for j in range(i, len(s)):
                substring = s[i:j+1]
                if is_palindrome(substring) and len(longest) < len(substring):
                    longest = substring
        
        return longest

