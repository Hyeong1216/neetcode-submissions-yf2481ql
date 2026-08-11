class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if len(t) > len(s):
            return ""
        
        countT = {}
        for c in t:
            countT[c] = countT.get(c, 0) + 1
        
        need, have = len(countT), 0
        res, resLen = [-1, -1], float('infinity')

        window = {}
        l = 0

        for r in range(len(s)):
            c = s[r]
            window[c] = window.get(c, 0) + 1


            if c in countT and window[c] == countT[c]: #c in countT (있냐), 그리고 window[c] == countT[c] (필요한 갯수만큼 있냐))
                have += 1
            
            while have == need:
                if r - l + 1 < resLen:
                    res = [l, r]
                    resLen = r-l+1
                window[s[l]] -= 1
                if s[l] in countT and window[s[l]] < countT[s[l]]:
                    have -=1
                l += 1
        l, r = res
        return s[l:r+1] if resLen != float("infinity") else ""































# class Solution:
#     def minWindow(self, s: str, t: str) -> str:
#         # questions
#         # 1. Can t be longer than s?
#         # 2. Any special characters?
#         # 3. Is the answer gurangeeed to exist?
#         # 4. Are there duplicate characters in t?
        
#         # solution
#         countT = {}
#         for c in t:
#             countT[c] = countT.get(c, 0) + 1
        
#         need, have = len(countT), 0
#         res, resLen = [-1, -1], float('infinity')

#         window = {}
#         l = 0
#         for r in range(len(s)):
#             c = s[r]
#             window[c] = window.get(c, 0) + 1

#             if c in countT and window[c] == countT[c]:
#                 have += 1

#             while have == need:
#                 if r-l+1 < resLen:
#                     res = [l, r]
#                     resLen = r-l+1
#                 window[s[l]] -= 1
#                 if s[l] in countT and window[s[l]] < countT[s[l]]:
#                     have -= 1
#                 l += 1


#         l, r = res
#         return s[l:r+1] if resLen != float('infinity') else ""



