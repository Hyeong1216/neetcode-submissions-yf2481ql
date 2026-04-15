class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        tMap = {}
        sMap = {}

        for i in range(len(s)):
            tMap[t[i]] = tMap.get(t[i], 0) + 1
            sMap[s[i]] = sMap.get(s[i], 0) + 1

        return tMap == sMap

        
            