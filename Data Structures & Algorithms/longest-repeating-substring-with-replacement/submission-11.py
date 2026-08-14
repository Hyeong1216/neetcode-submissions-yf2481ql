class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        maxF = 0
        l = 0
        count = {}

        for r in range(len(s)):
            c = s[r]
            count[c] = count.get(c, 0) + 1
            maxF = max(count[c], maxF)

            if r - l + 1 - maxF > k:
                # print(r - l + 1 - maxF, " triggered")
                count[s[l]] -= 1
                l += 1

    
        return len(s) - l























# class Solution:
#     def characterReplacement(self, s: str, k: int) -> int:
#         maxF = 0
#         l = 0
#         count = {}

#         for r in range(len(s)):
#             c = s[r]
#             count[c] = count.get(c, 0) + 1
#             maxF = max(maxF, count[c])

#             if (r-l+1) - maxF > k:
#                 count[s[l]] -= 1
#                 l += 1
#         return len(s) - l























# class Solution:
#     def characterReplacement(self, s: str, k: int) -> int:
#         l = 0
#         count = {}
#         maxF = float('-inf')

#         for r in range(len(s)):
#             count[s[r]] = count.get(s[r], 0) + 1
#             maxF = max(maxF, count[s[r]])

#             if (r-l+1) - maxF > k:
#                 count[s[l]] -= 1
#                 l += 1
        
#         return len(s) - l






























# class Solution:
#     def characterReplacement(self, s: str, k: int) -> int:
#         l = 0
#         maxF = 0
#         count = {}

#         for r in range(len(s)):
#             count[s[r]] = count.get(s[r], 0) + 1
#             maxF = max(maxF, count[s[r]])
#             if (r-l+1) - maxF > k:
#                 count[s[l]] -= 1
#                 l += 1

#         return len(s) - l