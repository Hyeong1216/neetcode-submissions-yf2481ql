class Solution:
    def longestPalindrome(self, s: str) -> str:
        # 1. brute force
        # def is_palindrome(substring):
        #     l, r = 0, len(substring) - 1
        #     while l < r:
        #         if substring[l] != substring[r]:
        #             return False
        #         l += 1
        #         r -= 1
        #     return True

        # longest = ""

        # for i in range(len(s)):
        #     for j in range(i, len(s)):
        #         substring = s[i:j+1]
        #         if is_palindrome(substring) and len(longest) < len(substring):
        #             longest = substring
        
        # return longest


        # 2. expand around the center
        # def expand_around_center(l, r):
        #     while(l >= 0 and r < len(s) and s[l] == s[r]):
        #         l -= 1
        #         r += 1

        #     return s[l+1:r]

        # longest = ""

        # for i in range(len(s)):
        #     odd_palindrome = expand_around_center(i, i)
        #     even_palindrome = expand_around_center(i, i + 1)

        #     if len(odd_palindrome) > len(longest):
        #         longest = odd_palindrome
        #     if len(even_palindrome) > len(longest):
        #         longest = even_palindrome
        
        # return longest


        # 3. Dynamic Programming
        n = len(s)
        dp = [[False] * n for _ in range(n)]
        start = 0
        max_len = 1
        
        #length 1 (always True)
        for i in range(n):
            dp[i][i] = True
        
        #length 2
        for i in range(n-1):
            if s[i] == s[i+1]:
                dp[i][i+1] = True
                start = i
                max_len = 2
        
        #length 3
        for length in range(3, n+1):
            for i in range(n-length+1):
                j = i + length - 1
                
                if (s[i] == s[j]) and dp[i+1][j-1]:
                    dp[i][j] = True
                    if length > max_len:
                        start = i
                        max_len = length
        return s[start:start+max_len]

        

        return longest