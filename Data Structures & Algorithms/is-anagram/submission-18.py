class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # 1. Sorting: O(nlogn+mlogm)
        if len(s) != len(t):
            return False
        return sorted(s) == sorted(t)
        #-----------------------------------------------

        # 2. Hash Map: O(n+m)









        #-----------------------------------------------

        # 3. Hash Table (Using Array)













        #-----------------------------------------------

        # 1. Sorting: O(nlogn+mlogm)
        # if len(s) != len(t):
        #     return False

        # return sorted(s) == sorted(t)
        #-----------------------------------------------
        # 2. Hash Map: O(n+m)
        # if len(s) != len(t):
        #     return False
        
        # sMap = {}
        # tMap = {}

        # for i in range(len(s)):
        #     sMap[s[i]] = sMap.get(s[i], 0) + 1
        #     tMap[t[i]] = tMap.get(t[i], 0) + 1

        # return sMap == tMap
        #-----------------------------------------------
        # 3. Hash Table (Using Array)
        # if len(s) != len(t):
        #     return False
        # count = [0] * 26
        # for i in range(len(s)):
        #     count[ord(s[i])-ord('a')] += 1
        #     count[ord(t[i])-ord('a')] -= 1
        # for val in count:
        #     if val != 0:
        #         return False
        # return True

        #-----------------------------------------------

        # if len(s) != len(t):
        #     return False
        # sMap = {}
        # for c in s:
        #     sMap[c] = sMap.get(c, 0) + 1
        # for c in t:
        #     if c not in sMap or sMap[c] == 0:
        #         return False
        #     sMap[c] = sMap[c] - 1
        # return True

        #-----------------------------------------------
