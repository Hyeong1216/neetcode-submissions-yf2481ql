class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        sMap = {}
        for c in s:
            sMap[c] = sMap.get(c, 0) + 1
        for c in t:
            if c not in sMap or sMap[c] == 0:
                return False
            sMap[c] = sMap[c] - 1
        return True