class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        def backtrack(current="", open_remain=n, close_remain=n, stack=[]):
            # 1. no more open and close addition available
            # Check if stack is empty, because it has to be to be a valid
            # otherwise return
            if open_remain == 0 and close_remain == 0:
                if not stack:
                    result.append(current)
                return
            
            # 2. if open_remain > 0
            if open_remain > 0:
                stack.append('(')
                backtrack(current + '(', open_remain-1, close_remain, stack)
                stack.pop()

            # 3. if close_remain > 0 and stack is not empty
            # meaning at least one opening bracket is present
            if close_remain > 0 and stack:
                stack.pop()
                backtrack(current + ')', open_remain, close_remain-1, stack)
                stack.append('(')

        result = []
        backtrack()
        return result