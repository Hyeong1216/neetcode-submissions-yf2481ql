class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        # Questions
        # 1. can there be numbers or special characters?
        # 2. Can the string be empty?
        # 3. Is it case sensitive?
        # 4. Can there be spaces?

        # answer
        l, res = 0, 0
        charSet = set()

        for r in range(len(s)):
            while s[r] in charSet:
                charSet.remove(s[l])
                l += 1
            charSet.add(s[r])
            res = max(r-l+1, res)
            # r += 1
        

        return res

        # O(n)