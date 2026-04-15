class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        tmap, smap = {}, {}
        for i in range(len(s)):
            tmap[t[i]] = tmap.get(t[i], 0) + 1
            smap[s[i]] = smap.get(s[i], 0) + 1
        return tmap == smap
            