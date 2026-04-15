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
        def expand_around_center(l, r):
            while(l >= 0 and r < len(s) and s[l] == s[r]):
                l -= 1
                r += 1

            return s[l+1:r]

        longest = ""

        for i in range(len(s)):
            odd_palindrome = expand_around_center(i, i)
            even_palindrome = expand_around_center(i, i + 1)

            if len(odd_palindrome) > len(longest):
                longest = odd_palindrome
            if len(even_palindrome) > len(longest):
                longest = even_palindrome
        
        return longest

