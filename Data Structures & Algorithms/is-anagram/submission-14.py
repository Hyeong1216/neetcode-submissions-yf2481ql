class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # 1. Sorting
        if len(s) != len(t):
            return False

        return sorted(s) == sorted(t)
        #-----------------------------------------------

        # 2. Hash Map

        #-----------------------------------------------

        # 3. Hash Map (Using Array)


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
