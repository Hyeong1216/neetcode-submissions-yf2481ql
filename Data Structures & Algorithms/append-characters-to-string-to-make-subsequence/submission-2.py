class Solution:
    def appendCharacters(self, s: str, t: str) -> int:
        # initial thought: traverse through t and check t element in s
        # if not from there len(t) minus that spot

        ptr = 0
        matching = 0
        for i in range(len(t)):
            c = t[i]
            while ptr < len(s) and s[ptr] != c:
                ptr += 1
            # either ptr is pointing to same char or to the None (end)
            if ptr < len(s) and s[ptr] == c:
                matching += 1
                ptr += 1
        
        return len(t) - matching
