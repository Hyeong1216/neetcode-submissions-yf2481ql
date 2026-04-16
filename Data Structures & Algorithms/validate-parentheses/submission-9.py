class Solution:
    def isValid(self, s: str) -> bool:
        Map = {"}":"{", ")":"(", "]":"["}
        stack = []

        for c in s:
            if c not in Map: #means opening
                stack.append(c)
                continue
            # when closing, because if it is closing
            # stack should not be empty,  
            # and it has to match the pair opening 
            if not stack or stack[-1] != Map[c]:
                return False
            stack.pop()
        return not stack