class Solution:
    def isPalindrome(self, s: str) -> bool:
        def is_letter(c):
            return c.isalnum()
        
        l, r = 0, len(s) - 1
        while l < r:
            if not is_letter(s[l]):
                l += 1
                continue
            if not is_letter(s[r]):
                r -= 1
                continue
            if s[l].upper() != s[r].upper():
                return False
            l += 1
            r -= 1
        return True