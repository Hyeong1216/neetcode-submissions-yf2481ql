class Solution:
    def isPalindrome(self, s: str) -> bool:
        # left right ptrs > set it to place
        # while > compare
        def is_letter(char):
            return char.isalnum()

        left = 0
        right = len(s) - 1
        while left <= right:
            # print(s[left], ", ", s[right])
            if not is_letter(s[left]):
                left += 1
                continue
            if not is_letter(s[right]):
                right -= 1
                continue
            
            if s[left].lower() != s[right].lower():
                return False
            left += 1
            right -= 1
        return True


        