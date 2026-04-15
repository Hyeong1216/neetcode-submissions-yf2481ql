class Solution:
    def isValid(self, s: str) -> bool:
        Map = {")":"(", "]":"[", "}":"{"}
        stack = []

        for c in s:
            if c not in Map: #opening
                stack.append(c)
                continue
            #if not opening, stack should be populated with at least one element
            #스택 최상단에 있는게 맵에 있는것과 일치하지 않으면
            if not stack or stack[-1] != Map[c]:
                return False
            stack.pop()
        return not stack
                
