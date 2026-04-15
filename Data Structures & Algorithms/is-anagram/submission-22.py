class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # 1. Sorting
        # if len(s) != len(t):
        #     return False
        # return sorted(s) == sorted(t)

        # 2. Hash Map
        # if len(s) != len(t):
        #     return False
        # sMap = {}
        # tMap = {}

        # for i in range(len(s)):
        #     sMap[s[i]] = sMap.get(s[i], 0) + 1
        #     tMap[t[i]] = tMap.get(t[i], 0) + 1
            
        # return sMap == tMap

        # 3. Hash Table (using array)
        if len(s) != len(t):
            return False
        count = [0] * 26
        for i in range(len(s)):
            count[ord(s[i])-ord('a')] += 1
            count[ord(t[i])-ord('a')] -= 1
        for value in count:
            if value != 0:
                return False
        return True
