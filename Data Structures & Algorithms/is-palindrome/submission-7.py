class Solution:
    def isPalindrome(self, s: str) -> bool:
        def is_letter(c):
            return c.isalnum()
        l, r= 0, len(s) - 1
        while l<r:
            if not is_letter(s[l]):
                l += 1
                continue
            if not is_letter(s[r]):
                r -= 1
                continue
            if s[l].lower() != s[r].lower():
                return False
            l += 1
            r -= 1
        return True
        
        
        
        
        
        
        
        
        
        
        #------------------
        # left right ptrs > set it to place
        # while > compare
        # def is_letter(char):
        #     return char.isalnum()

        # left = 0
        # right = len(s) - 1
        # while left < right:
        #     # print(s[left], ", ", s[right])
        #     if not is_letter(s[left]):
        #         left += 1
        #         continue
        #     if not is_letter(s[right]):
        #         right -= 1
        #         continue
            
        #     if s[left].lower() != s[right].lower():
        #         return False
        #     left += 1
        #     right -= 1
        # return True


        