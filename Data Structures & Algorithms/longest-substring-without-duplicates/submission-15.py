class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        # r expand until it sees repeated character
        # if it sees repeated character, decrease from count set
        # and increment l
        l, res = 0, 0
        charSet = set()

        for r in range(len(s)):
            while s[r] in charSet:
                charSet.remove(s[l])
                l += 1
            charSet.add(s[r])
            res = max(r - l + 1, res)

    
        return res




























# class Solution:
#     def lengthOfLongestSubstring(self, s: str) -> int:
#         # Questions
#         # 1. can there be numbers or special characters?
#         # 2. Can the string be empty?
#         # 3. Is it case sensitive?
#         # 4. Can there be spaces?

#         # answer
#         l, res = 0, 0
#         charSet = set()

#         for r in range(len(s)):
#             while s[r] in charSet:
#                 charSet.remove(s[l])
#                 l += 1
#             charSet.add(s[r])
#             res = max(r-l+1, res)
            
#         return res

#         # O(n)