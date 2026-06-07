class Solution:
    def prefixCount(self, words: List[str], pref: str) -> int:
        count = 0
        if len(pref) == 0:
            return len(words)
        
        for word in words:
            if word[:len(pref)] == pref:
                count += 1
        return count
        