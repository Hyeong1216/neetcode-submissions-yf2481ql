class Solution:
    def countSubstrings(self, s: str) -> int:
        # 1. brute force
        # def is_palindrome(substring):
        #     l, r = 0, len(substring) - 1
        #     while l < r:
        #         if substring[l] != substring[r]:
        #             return False
        #         l += 1
        #         r -= 1
        #     return True

        # count = 0

        # for i in range(len(s)):
        #     for j in range(i, len(s)):
        #         substring = s[i:j+1]
        #         if is_palindrome(substring):
        #             count += 1
        
        # return count


        # 2. expand around the center
        # def expand_around_center(l, r):
        #     count = 0
            
        #     while(l >= 0 and r < len(s) and s[l] == s[r]):
        #         count += 1
        #         l -= 1
        #         r += 1


        #     return count

        # total_count = 0

        # for i in range(len(s)):
        #     total_count += expand_around_center(i, i)
        #     total_count += expand_around_center(i, i + 1)

        # return total_count


        # # 3. Dynamic Programming
        n = len(s)
        dp = [[False] * n for _ in range(n)]
        count = 0
        
        #length 1 (always True)
        for i in range(n):
            dp[i][i] = True
            count += 1
        
        #length 2
        for i in range(n-1):
            if s[i] == s[i+1]:
                dp[i][i+1] = True
                count += 1
        
        #length 3
        for length in range(3, n+1):
            for i in range(n-length+1):
                j = i + length - 1
                
                if (s[i] == s[j]) and dp[i+1][j-1]:
                    dp[i][j] = True
                    count += 1

        return count

        # 4. Manacher's Algorithm
        # processed = "#".join("^{}$".format(s))
        # n = len(processed)
        # P = [0] * n             # P[i] = radius of palindrome centered at i
        # center = 0              # Center of rightmost palindrome
        # right = 0               # Right boundary of rightmost palindrome

        # for i in range(1, n-1): # Skip sentinels ^ and $
        #     mirror_i = 2 * center - i

        #     if i < right:
        #         # we can use information from mirror position
        #         P[i] = min(right - i, P[mirror_i])
        #     # If i >= right, we start with P[i] = 0 (default)
            
